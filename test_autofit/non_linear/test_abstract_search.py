import pickle
import shutil
from os import path

import numpy as np
import pytest

import autofit as af
from autoconf import conf
from autofit.mock import mock

pytestmark = pytest.mark.filterwarnings("ignore::FutureWarning")


@pytest.fixture(name="mapper")
def make_mapper():
    return af.ModelMapper()


@pytest.fixture(name="mock_list")
def make_mock_list():
    return [af.PriorModel(mock.MockClassx4), af.PriorModel(mock.MockClassx4)]


class TestLabels:
    def test_param_names(self):
        model = af.PriorModel(mock.MockClassx4)
        assert [
                   "one",
                   "two",
                   "three",
                   "four",
               ] == model.model_component_and_parameter_names

    def test_label_config(self):
        assert conf.instance["notation"]["label"]["label"]["one"] == "one_label"
        assert conf.instance["notation"]["label"]["label"]["two"] == "two_label"
        assert conf.instance["notation"]["label"]["label"]["three"] == "three_label"
        assert conf.instance["notation"]["label"]["label"]["four"] == "four_label"


test_path = path.join(
    "{}".format(path.dirname(path.realpath(__file__))), "files", "phase"
)


class TestMovePickleFiles:
    def test__move_pickle_files(self):

        search = af.MockSearch(paths=af.Paths(name="pickles", path_prefix=path.join("non_linear", "abstract_search")))

        pickle_paths = [
            path.join(
                conf.instance.output_path, "non_linear", "abstract_search", "pickles"
            )
        ]

        arr = np.ones((3, 3))

        with open(path.join(pickle_paths[0], "test.pickle"), "wb") as f:
            pickle.dump(arr, f)

        pickle_paths = [
            path.join(
                conf.instance.output_path,
                "non_linear",
                "abstract_search",
                "pickles",
                "test.pickle",
            )
        ]

        search.paths._move_pickle_files(pickle_files=pickle_paths)

        with open(path.join(pickle_paths[0]), "rb") as f:
            arr_load = pickle.load(f)

        assert (arr == arr_load).all()

        if path.exists(test_path):
            shutil.rmtree(test_path)