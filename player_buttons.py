class PlayerButtons:
    def __init__(self, page, ft):
        self.page = page
        self.ft = ft
        self.track = ""
        self.player = None
        self.play_pause_button = None
        self.duration_slider = None
        self.time_text = None
        self._update_timer = None

    async def play_track(self, e):
        if self.player and self.player.song:
            if self.player._is_playing and self.player.song.button_name == self.track:
                # Если играет тот же трек - ставим на паузу
                self.player.pause()
                self.play_pause_button.icon = self.ft.Icons.PLAY_CIRCLE
                self.stop_timer()
            else:
                # Если другой трек или на паузе - играем
                await self.player.play()
                self.play_pause_button.icon = self.ft.Icons.PAUSE_CIRCLE
                self.start_timer()
            self.page.update()

    def start_timer(self):
        self.stop_timer()  # Останавливаем предыдущий таймер если есть
        self._update_timer = self.page.window_to_front()
        self.update_slider()

    def stop_timer(self):
        if self._update_timer:
            self._update_timer = None

    def update_slider(self):
        if self.player and self.player.song and self.player._is_playing:
            current_time = self.player.get_position()
            duration = self.player.get_duration()
            if duration > 0:
                self.duration_slider.value = (current_time / duration) * 100
                self.time_text.value = f"{int(current_time)} / {int(duration)}"
                self.page.update()


    def on_slider_change(self, e):
        if self.player and self.player.song:
            duration = self.player.get_duration()
            if duration > 0:
                position = (e.control.value / 100) * duration
                self.player.seek(position)

    def build_player_buttons(self):
        left_button = self.ft.IconButton(icon=self.ft.Icons.ARROW_CIRCLE_LEFT, on_click = self.click_previous_track, icon_size=30, tooltip="Previous track")
        right_button = self.ft.IconButton(icon=self.ft.Icons.ARROW_CIRCLE_RIGHT,  on_click = self.click_next_track, icon_size=30, tooltip="Next track")
        self.play_pause_button = self.ft.IconButton(
            icon= self.ft.Icons.PLAY_CIRCLE if self.player._is_playing == False else self.ft.Icons.PAUSE_CIRCLE ,
            on_click=self.play_track,
            icon_size=40,
            tooltip="Play/Pause"
        )

        self.time_text = self.ft.Text("0 / 0")
        self.duration_slider = self.ft.Slider(
            min=0,
            max=100,
            value=0,
            on_change=self.on_slider_change
        )

        row = self.ft.Row(
            [left_button, self.play_pause_button, right_button],
            alignment=self.ft.MainAxisAlignment.CENTER,
            spacing=20
        )
        c = self.ft.Column([
            self.ft.Text(self.track, size=16, weight=self.ft.FontWeight.BOLD),
            row,
            self.time_text,
            self.duration_slider
        ])
        self.page.add(c)

    async def click_next_track(self, e):
        while len(self.page.controls) > 2:
            self.page.controls.pop()
        self.track = self.player.next_track
        self.player.new_track( self.player.next_track)
        await self.player.play()
        self.build_player_buttons()
        self.page.update()

    async def click_previous_track(self, e):

        while len(self.page.controls) > 2:
            self.page.controls.pop()
        self.track = self.player.previous_track

        self.player.new_track(self.player.previous_track)
        await self.player.play()
        self.build_player_buttons()
        self.page.update()