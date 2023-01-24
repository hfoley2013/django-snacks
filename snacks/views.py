from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/2019-04-01_23_16_02_Lay%27s_Classic_Potato_Chips_in_the_Dulles_section_of_Sterling%2C_Loudoun_County%2C_Virginia.jpg/1920px-2019-04-01_23_16_02_Lay%27s_Classic_Potato_Chips_in_the_Dulles_section_of_Sterling%2C_Loudoun_County%2C_Virginia.jpg",
                "title": "Lay's Potato Chips",
                "description": "They're called chips, not chip, for a reason.",
                "reference_url": "https://en.wikipedia.org/wiki/Lay's"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Hostess-Twinkies.jpg/1920px-Hostess-Twinkies.jpg",
                "title": "Twinkies",
                "description": "Only thing in the world that will outlive the cockroach.",
                "reference_url": "https://en.wikipedia.org/wiki/Twinkie"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Skittles-Louisiana-2003.jpg/220px-Skittles-Louisiana-2003.jpg",
                "title": "Skittles",
                "description": "Taste the rainbow.",
                "reference_url": "https://en.wikipedia.org/wiki/Skittles_(confectionery)"
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'
