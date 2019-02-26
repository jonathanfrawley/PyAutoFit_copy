import logging

from autofit import exc

logger = logging.getLogger(__name__)


class ResultsCollection(object):
    def __init__(self):
        self.__result_list = []
        self.__result_dict = {}

    @property
    def last(self):
        if len(self.__result_list) > 0:
            return self.__result_list[-1]
        return None

    @property
    def first(self):
        if len(self.__result_list) > 0:
            return self.__result_list[0]
        return None

    def add(self, phase_name, result):
        self.__result_list.append(result)
        self.__result_dict[phase_name] = result

    def from_phase(self, phase_name):
        try:
            return self.__result_dict[phase_name]
        except KeyError:
            raise exc.PipelineException("No previous phase named {} found in results ({})".format(phase_name, ", ".join(
                self.__result_dict.keys())))


class Pipeline(object):

    def __init__(self, pipeline_name, *phases):
        """

        Parameters
        ----------
        pipeline_name: str
            The phase_name of this pipeline
        """
        self.pipeline_name = pipeline_name
        self.phases = phases

    def __add__(self, other):
        """
        Compose two runners

        Parameters
        ----------
        other: Pipeline
            Another pipeline

        Returns
        -------
        composed_pipeline: Pipeline
            A pipeline that runs all the  phases from this pipeline and then all the phases from the other pipeline
        """
        return self.__class__("{} + {}".format(self.pipeline_name, other.pipeline_name), *(self.phases + other.phases))

    def run_function(self, func):
        results = ResultsCollection()
        for i, phase in enumerate(self.phases):
            logger.info("Running Phase {} (Number {})".format(phase.optimizer.name, i))
            results.add(phase.phase_name, func(phase, results))
        return results
