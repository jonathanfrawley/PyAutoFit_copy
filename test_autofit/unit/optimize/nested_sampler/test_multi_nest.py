import os
import shutil
from functools import wraps

import pytest

from autoconf import conf
import autofit as af
from autofit.optimize.non_linear.nested_sampling import multi_nest as mn
from test_autofit.mock import MockClassNLOx4

directory = os.path.dirname(os.path.realpath(__file__))
pytestmark = pytest.mark.filterwarnings("ignore::FutureWarning")


@pytest.fixture(autouse=True)
def set_config_path():
    conf.instance = conf.Config(
        config_path=os.path.join(directory, "files/multinest/config"),
        output_path=os.path.join(directory, "files/multinest/output"),
    )


@pytest.fixture(name="multi_nest_summary_path")
def test_multi_nest_summary():
    multi_nest_summary_path = "{}/files/multinest/summary".format(
        os.path.dirname(os.path.realpath(__file__))
    )

    if os.path.exists(multi_nest_summary_path):
        shutil.rmtree(multi_nest_summary_path)

    os.mkdir(multi_nest_summary_path)

    return multi_nest_summary_path


@pytest.fixture(name="multi_nest_samples_path")
def test_multi_nest_samples():
    multi_nest_samples_path = "{}/files/multinest/samples".format(
        os.path.dirname(os.path.realpath(__file__))
    )

    if os.path.exists(multi_nest_samples_path):
        shutil.rmtree(multi_nest_samples_path)

    os.mkdir(multi_nest_samples_path)

    return multi_nest_samples_path


@pytest.fixture(name="multi_nest_resume_path")
def test_multi_nest_resume():
    multi_nest_resume_path = "{}/files/multinest/resume".format(
        os.path.dirname(os.path.realpath(__file__))
    )

    if os.path.exists(multi_nest_resume_path):
        shutil.rmtree(multi_nest_resume_path)

    os.mkdir(multi_nest_resume_path)

    return multi_nest_resume_path


def create_path(func):
    @wraps(func)
    def wrapper(path):
        if not os.path.exists(path):
            os.makedirs(path)
        return func(path)

    return wrapper


@create_path
def create_summary_4_parameters(path):
    summary = open(path + "/multinestsummary.txt", "w")
    summary.write(
        "    0.100000000000000000E+01   -0.200000000000000000E+01    0.300000000000000000E+01"
        "    0.400000000000000000E+01   -0.500000000000000000E+01    0.600000000000000000E+01"
        "    0.700000000000000000E+01    0.800000000000000000E+01"
        "    0.900000000000000000E+01   -1.000000000000000000E+01   -1.100000000000000000E+01"
        "    1.200000000000000000E+01    1.300000000000000000E+01   -1.400000000000000000E+01"
        "   -1.500000000000000000E+01    1.600000000000000000E+01"
        "    0.020000000000000000E+00    0.999999990000000000E+07"
        "    0.020000000000000000E+00    0.999999990000000000E+07\n"
    )
    summary.write(
        "    0.100000000000000000E+01   -0.200000000000000000E+01    0.300000000000000000E+01"
        "    0.400000000000000000E+01   -0.500000000000000000E+01    0.600000000000000000E+01"
        "    0.700000000000000000E+01    0.800000000000000000E+01"
        "    0.900000000000000000E+01   -1.000000000000000000E+01   -1.100000000000000000E+01"
        "    1.200000000000000000E+01    1.300000000000000000E+01   -1.400000000000000000E+01"
        "   -1.500000000000000000E+01    1.600000000000000000E+01"
        "    0.020000000000000000E+00    0.999999990000000000E+07"
    )
    summary.close()


@create_path
def create_weighted_samples_4_parameters(path):
    with open(path + "/multinest.txt", "w+") as weighted_samples:
        weighted_samples.write(
            "    0.020000000000000000E+00    0.999999990000000000E+07    0.110000000000000000E+01    "
            "0.210000000000000000E+01    0.310000000000000000E+01    0.410000000000000000E+01\n"
            "    0.020000000000000000E+00    0.999999990000000000E+07    0.090000000000000000E+01    "
            "0.190000000000000000E+01    0.290000000000000000E+01    0.390000000000000000E+01\n"
            "    0.010000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n"
            "    0.050000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n"
            "    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n"
            "    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n"
            "    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n"
            "    0.100000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n"
            "    0.200000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01\n"
            "    0.300000000000000000E+00    0.999999990000000000E+07    0.100000000000000000E+01    "
            "0.200000000000000000E+01    0.300000000000000000E+01    0.400000000000000000E+01"
        )


@create_path
def create_resume(path):
    with open(path + "/multinestresume.dat", "w+") as resume:
        resume.write(
            " F\n"
            "        3000       12345           1          50\n"
            "    0.502352236277967168E+05    0.502900436569068333E+05\n"
            " T\n"
            "   0\n"
            " T F     0          50\n"
            "    0.648698272260014622E-26    0.502352236277967168E+05    0.502900436569068333E+05\n"
        )


class TestMulitNest:
    def test__loads_from_config_file_if_not_input(self):

        multi_nest = af.MultiNest(
            n_live_points=40,
            sampling_efficiency=0.5,
            const_efficiency_mode=True,
            evidence_tolerance=0.4,
            importance_nested_sampling=False,
            multimodal=False,
            n_iter_before_update=90,
            null_log_evidence=-1.0e80,
            max_modes=50,
            mode_tolerance=-1e88,
            seed=0,
            verbose=True,
            resume=False,
            context=1,
            write_output=False,
            log_zero=-1e90,
            max_iter=1,
            init_MPI=True,
            terminate_at_acceptance_ratio=True,
            acceptance_ratio_threshold=0.9,
        )

        assert multi_nest.n_live_points == 40
        assert multi_nest.sampling_efficiency == 0.5
        assert multi_nest.const_efficiency_mode == True
        assert multi_nest.evidence_tolerance == 0.4
        assert multi_nest.importance_nested_sampling == False
        assert multi_nest.multimodal == False
        assert multi_nest.n_iter_before_update == 90
        assert multi_nest.null_log_evidence == -1e80
        assert multi_nest.max_modes == 50
        assert multi_nest.mode_tolerance == -1e88
        assert multi_nest.seed == 0
        assert multi_nest.verbose == True
        assert multi_nest.resume == False
        assert multi_nest.context == 1
        assert multi_nest.write_output == False
        assert multi_nest.log_zero == -1e90
        assert multi_nest.max_iter == 1
        assert multi_nest.init_MPI == True
        assert multi_nest.terminate_at_acceptance_ratio == True
        assert multi_nest.acceptance_ratio_threshold == 0.9

        multi_nest = af.MultiNest()

        assert multi_nest.importance_nested_sampling == True
        assert multi_nest.multimodal == True
        assert multi_nest.const_efficiency_mode == False
        assert multi_nest.n_live_points == 50
        assert multi_nest.evidence_tolerance == 0.5
        assert multi_nest.sampling_efficiency == 0.6
        assert multi_nest.n_iter_before_update == 100
        assert multi_nest.null_log_evidence == -1e90
        assert multi_nest.max_modes == 100
        assert multi_nest.mode_tolerance == -1e89
        assert multi_nest.seed == -1
        assert multi_nest.verbose == False
        assert multi_nest.resume == True
        assert multi_nest.context == 0
        assert multi_nest.write_output == True
        assert multi_nest.log_zero == -1e100
        assert multi_nest.max_iter == 0
        assert multi_nest.init_MPI == False
        assert multi_nest.terminate_at_acceptance_ratio == False
        assert multi_nest.acceptance_ratio_threshold == 1.0

        model = af.ModelMapper(mock_class_1=MockClassNLOx4)

        fitness = af.MultiNest.Fitness(
            paths=multi_nest.paths,
            analysis=None,
            model=model,
            samples_from_model=multi_nest.samples_from_model,
            terminate_at_acceptance_ratio=False,
            acceptance_ratio_threshold=0.0,
            stagger_resampling_likelihood=False,
        )

        assert fitness.model_results_output_interval == 100
        assert fitness.model == model
        assert fitness.terminate_at_acceptance_ratio == False
        assert fitness.acceptance_ratio_threshold == 0.0

    @staticmethod
    def assert_non_linear_attributes_equal(copy):
        assert copy.paths.name == "phase_name/one"

    def test__copy_with_name_extension(self):
        optimizer = af.MultiNest(af.Paths("phase_name"), sigma=2.0)

        copy = optimizer.copy_with_name_extension("one")
        self.assert_non_linear_attributes_equal(copy)
        assert isinstance(copy, af.MultiNest)
        assert copy.sigma is optimizer.sigma
        assert copy.importance_nested_sampling is optimizer.importance_nested_sampling
        assert copy.multimodal is optimizer.multimodal
        assert copy.const_efficiency_mode is optimizer.const_efficiency_mode
        assert copy.n_live_points is optimizer.n_live_points
        assert copy.evidence_tolerance is optimizer.evidence_tolerance
        assert copy.sampling_efficiency is optimizer.sampling_efficiency
        assert copy.n_iter_before_update is optimizer.n_iter_before_update
        assert copy.null_log_evidence is optimizer.null_log_evidence
        assert copy.max_modes is optimizer.max_modes
        assert copy.mode_tolerance is optimizer.mode_tolerance
        assert copy.seed is optimizer.seed
        assert copy.verbose is optimizer.verbose
        assert copy.resume is optimizer.resume
        assert copy.context is optimizer.context
        assert copy.write_output is optimizer.write_output
        assert copy.log_zero is optimizer.log_zero
        assert copy.max_iter is optimizer.max_iter
        assert copy.init_MPI is optimizer.init_MPI
        assert (
            copy.terminate_at_acceptance_ratio
            is optimizer.terminate_at_acceptance_ratio
        )
        assert copy.acceptance_ratio_threshold is optimizer.acceptance_ratio_threshold

    def test__read_quantities_from_weighted_samples_file(self, multi_nest_samples_path):
        conf.instance.output_path = multi_nest_samples_path + "/1_class"

        multi_nest = af.MultiNest()

        create_weighted_samples_4_parameters(path=multi_nest.paths.backup_path)

        parameters = mn.parameters_from_file_weighted_samples(
            file_weighted_samples=f"{multi_nest.paths.backup_path}/multinest.txt",
            prior_count=4,
        )

        assert parameters == [
            [1.1, 2.1, 3.1, 4.1],
            [0.9, 1.9, 2.9, 3.9],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
        ]

        log_likelihoods = mn.log_likelihoods_from_file_weighted_samples(
            file_weighted_samples=f"{multi_nest.paths.backup_path}/multinest.txt"
        )

        value = -0.5 * 9999999.9

        assert log_likelihoods == 10 * [value]

        weights = mn.weights_from_file_weighted_samples(
            file_weighted_samples=f"{multi_nest.paths.backup_path}/multinest.txt"
        )

        assert weights == [0.02, 0.02, 0.01, 0.05, 0.1, 0.1, 0.1, 0.1, 0.2, 0.3]

    def test__read_total_samples_from_file_resume(self, multi_nest_resume_path):
        conf.instance.output_path = multi_nest_resume_path + "/1_class"

        multi_nest = af.MultiNest()

        create_resume(path=multi_nest.paths.backup_path)

        total_samples = mn.total_samples_from_file_resume(
            file_resume=f"{multi_nest.paths.backup_path}/multinestresume.dat"
        )

        assert total_samples == 12345

    def test__log_evidence_from_file_summary(self, multi_nest_summary_path):
        conf.instance.output_path = multi_nest_summary_path + "/1_class"

        multi_nest = af.MultiNest()

        log_evidence = mn.log_evidence_from_file_summary(
            file_summary=f"{multi_nest.paths.backup_path}/multinestsummary.txt",
            prior_count=4,
        )

        assert log_evidence == -1e99

        create_summary_4_parameters(path=multi_nest.paths.backup_path)

        log_evidence = mn.log_evidence_from_file_summary(
            file_summary=f"{multi_nest.paths.backup_path}/multinestsummary.txt",
            prior_count=4,
        )

        assert log_evidence == 0.02

    def test__samples_from_model(
        self, multi_nest_samples_path, multi_nest_resume_path, multi_nest_summary_path
    ):
        conf.instance.output_path = multi_nest_samples_path + "/1_class"

        multi_nest = af.MultiNest()

        create_weighted_samples_4_parameters(path=multi_nest.paths.backup_path)
        create_resume(path=multi_nest.paths.backup_path)
        create_summary_4_parameters(path=multi_nest.paths.backup_path)

        model = af.ModelMapper(mock_class=MockClassNLOx4)
        model.mock_class.two = af.LogUniformPrior(lower_limit=0.0, upper_limit=10.0)

        samples = multi_nest.samples_from_model(model=model)

        assert samples.parameters == [
            [1.1, 2.1, 3.1, 4.1],
            [0.9, 1.9, 2.9, 3.9],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
            [1.0, 2.0, 3.0, 4.0],
        ]

        value = -0.5 * 9999999.9

        assert samples.log_likelihoods == 10 * [value]
        assert samples.log_priors == pytest.approx(
            [0.243902, 0.256410, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25], 1.0e-4
        )
        assert samples.weights == [0.02, 0.02, 0.01, 0.05, 0.1, 0.1, 0.1, 0.1, 0.2, 0.3]
        assert samples.total_samples == 12345
        assert samples.log_evidence == 0.02
        assert samples.number_live_points == 50
