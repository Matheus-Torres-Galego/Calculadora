from qt_material import apply_stylesheet

extra = {"danger": "#dc3545"}


def Theme(self):
    apply_stylesheet(self, theme="dark_blue.xml", invert_secondary=True, extra=extra)
