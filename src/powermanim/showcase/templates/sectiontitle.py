from powermanim import SectionTitle
from powermanim.showcase.showcasescene import ShowcaseScene


class SectionTitleShowcase(ShowcaseScene):
    def showcasing():
        return SectionTitle

    def construct(self):
        title = SectionTitle("Section Title")
        self.play(title.show())
        self.wait(1)
        self.play(title.hide())
        self.wait(1)
