from powermanim.showcase.showcasescene import ShowcaseScene
from powermanim.templates.sectiontitle import SectionTitle


class SectionTitleShowcase(ShowcaseScene):
    def showcasing():
        return SectionTitle

    def construct(self):
        title = SectionTitle("Section Title")
        title.show(self)
        self.wait(1)
        title.hide(self)
        self.wait(1)
