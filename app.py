import os

import snorkel

from snorkel.web import app
from snorkel.presenter import DatasetPresenter, RegisterPresenter

from snorkel.views import ViewSeparator

from snorkel.plugins.snorkel_basic_views import TableView, TimeView, DistView, SamplesView
from snorkel.plugins.snorkel_basic_views import AreaView, ScatterView, BarView, GroupedDist
from snorkel.plugins.snorkel_advanced_views import TimelineView, OverviewView, ForecastView, DrilldownView
from snorkel.plugins.snorkel_advanced_views import DigraphView, WecoView

def configure_presenters():
    default_presenter = DatasetPresenter()
    default_presenter.set_views([
        TableView,
        TimeView,
        DistView,
        SamplesView,
        TimelineView,
        OverviewView,
        ViewSeparator,
        AreaView,
        BarView,
        ScatterView,
        GroupedDist,
        ViewSeparator,
        DigraphView,
        ViewSeparator,
        WecoView,
        ForecastView,
        DrilldownView

    ])
    RegisterPresenter(".*", default_presenter)


if __name__ == "__main__":
    from snorkel import web
    from snorkel import models

    models.create_db_if_not()

    configure_presenters()
    web.app.run(port=os.environ.get('PORT', 2333), use_reloader=False)
