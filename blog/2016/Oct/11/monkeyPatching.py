def toggle(self):
    if self.isVisible():
        self.hide()
    else:
        self.show()

widget.setsView.__class__.toggle = toggle

widget.setsView.toggle()
