import sounddevice as sd
import soundfile as sf
from io import BytesIO

class MusicPlayer:
    music_dict = {}


    def __init__(self):
        self.song = None
        self._is_playing = False
        self._current_position = 0
        self._audio_data = None
        self._samplerate = None
        self.next_track = None
        self.previous_track = None

    def new_track(self, track_id):
        self.song = self.music_dict[track_id]
        self._audio_data = None
        self._current_position = 0
        self._is_playing = False
        self.set_previous_next_tracks()


    async def play(self):
        """Play the track from the beginning or resume from pause."""
        if self.song._track_bytes is None:
            await self.song.download_song()

        if self._audio_data is None:
            audio_io = BytesIO(self.song._track_bytes)
            self._audio_data, self._samplerate = sf.read(audio_io)

        if not self._is_playing:
            sd.play(self._audio_data[self._current_position:], self._samplerate)
            self.song._is_playing = True

    def pause(self):
        """Pause the current playback."""
        if self._is_playing:
            sd.stop()
            self._is_playing = False
            # Сохраняем текущую позицию
            self._current_position = sd.get_stream().time * self._samplerate

    def stop(self):
        """Stop playback and reset position."""
        sd.stop()
        self._is_playing = False
        self._current_position = 0

    def seek(self, position_seconds: float):
        """Seek to specific position in the track."""
        if self._audio_data is not None:
            position_samples = int(position_seconds * self._samplerate)
            self._current_position = min(position_samples, len(self._audio_data))
            if self._is_playing:
                self.stop()
                self.play()

    def get_position(self) -> float:
        """Get current playback position in seconds."""
        if self._is_playing:
            return self._current_position / self._samplerate
        return 0.0

    def get_duration(self) -> float:
        """Get total duration of the track in seconds."""
        if self._audio_data is not None:
            return len(self._audio_data) / self._samplerate
        return 0.0

    def set_volume(self, volume: float):
        """Set playback volume (0.0 to 1.0)."""
        if 0.0 <= volume <= 1.0:
            sd.default.device[1] = volume

    def set_previous_next_tracks(self):
        track_list = list(self.music_dict.keys())
        current_track = track_list.index(self.song.button_name)
        self.next_track = track_list[(current_track + 1
                                                if (current_track +1) <= len(track_list) else 0)]

        self.previous_track = track_list[(current_track - 1
                                          if (current_track - 1) >= 0 else len(track_list) - 1)]
