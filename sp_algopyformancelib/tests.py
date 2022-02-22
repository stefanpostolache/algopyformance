
from __future__ import annotations
import inspect
from enum import Enum
from timeit import repeat
import numpy as np
import pandas as pd
from inspect import getargspec
import seaborn as sns
import matplotlib.pyplot as plt

"""
A Module that helps test the performance your algorithms. It provides a simple, 
developer friendly way to declare your tests and plot the results. 
"""


def show_performance_plot(df):
    """
    A function that turns any dataframe used to store performance data regarding
    performance tests into a graph.

    If the functions tested contain only one parameter, a relationship plot
    between the duration and that parameter will be plotted. If, however,
    the functions receive multiple arguments than a pair plot is built relating each
    individual parameter with the duration and eachother (see see seaborn
    pairplot) for more information.

    :param df: a data frame with keys (columns) ['algorithm', ...<function
    param names>, 'duration']
    :return:
    """
    sns.set_style("darkgrid")
    if df.shape[1] == 3:
        sns.relplot(data=df, x=df.columns[1], y='duration',
                    kind='line', hue='algorithm', palette='rocket_r')
    else:
        sns.pairplot(data=df, hue='algorithm', palette='rocket_r')
    plt.show()


class Test:
    """A class containing a single test

    Each test comprises the invocation of a single function passed as target
    and a single argument composition passed as payload.
    """

    def __init__(self, target, payload, repetitions):
        """
        Constructor of the Test class
        :param target: the function that is to be tested
        :param payload: parameters to run the class with
        """
        self.__target = target
        self.__payload = payload
        self.__repetitions = repetitions

    @property
    def target(self):
        return self.__target

    @property
    def payload(self):
        return self.__payload

    def run(self):
        """
        Executes the target function with the provided values for its
        parameters and times the execution
        :return: the duration of the execution
        """
        return sum(repeat(lambda: self.__target(*self.__payload),
                          number=1, repeat=self.__repetitions))/self.__repetitions


class TestStack:
    """
    A class that manages a stack of tests of the performance of your algorithm(s).

    This class enables you to run and compare the performance of different
    your algorithms. The class runs a set of tests on your algorithm(s) with
    various parameters and retrieves the durations for each execution.
    """

    def __init__(self, builder: TestStackBuilder):
        """
        Constructor of the TestStack class.
        :param builder: A TestStackBuilder instance used to set the attributes
        of the class
        """
        self.__should_show_plot = builder.plot
        self.__tests = builder.tests
        self.__params = builder.params
        self.__func_names = builder.func_names

    def run(self):
        """
        Runs the tests that the instance manages and retrieves the results in
        the form specified in output.
        :return: a dataframe with results from tests. Each test is described by the algorithm,
        the value for each parameter and the resulting duration of executing
        the script.
        """
        assert self.__tests, "No tests were added. Make sure you added targets while building the stack."

        results = pd.DataFrame(
            data=list(map(lambda row: list(map(lambda test: test.run(), row)), self.__tests)),
            index=self.__params,
            columns=self.__func_names
        )
        if self.__should_show_plot:
            results.plot(figsize=[15, 10])
            plt.show()

        return results


class TestStackBuilder:
    """
    A builder class for the TestStack class.

    Parameters
    ----------
    __plot (bool): whether to plot or not the results of the running the TestStack
    __targets (list(function)): list of functions to test.
    __param_combinations: list of parameter combinations to test the target
    functions with

    note that if you provide multiple targets they should have the same parameters
    """

    def __init__(self):
        self.__plot: bool = False
        self.__targets = []
        self.__param_combinations = []
        self.__repetitions = 1

    @property
    def plot(self) -> bool:
        """
        Getter of the __plot attribute
        :return: the value of the __plot attribute
        """
        return self.__plot

    @property
    def tests(self) -> list[list[Test]]:
        """
        Gets the tests as combinations of target functions and their respective parameters
        :return: A list of Tests
        """
        return [[Test(target, param_combination, self.__repetitions) for target in self.__targets] for param_combination in self.__param_combinations]

    @property
    def params(self) -> pd.MultiIndex:
        """
        Retrieves parameters used to test the functions as a MultiIndex for a dataframe
        :return: MultiIndex of parameter combinations
        """
        param_names = inspect.signature(self.__targets[0]).parameters.keys()
        return pd.MultiIndex.from_tuples(self.__param_combinations, names=param_names)

    @property
    def func_names(self) -> [str]:
        """
        Retrieves a list of names of functions tested
        :return: list of function names
        """
        return [func.__name__ for func in self.__targets]

    def add_target(self, target) -> TestStackBuilder:
        """
        Add function as target of tests.

        :param target: a function to check performance of
        :return: TestStackBuilder with additional target
        """
        self.__targets.append(target)
        return self

    def add_targets(self, targets) -> TestStackBuilder:
        """
        Add multiple functions as targets
        :param targets: list of functions to add as targets for the test
        :return: TestStackBuilder with additional targets
        """
        self.__targets.extend(targets)
        return self

    def add_param_combination(self, param_combination: tuple) -> TestStackBuilder:
        """
        Adds a combination of values for the parameters that the target(s)
        receive.

        :param param_combination: a tuple containing a combination of values for the parameters
        :return: a builder with the added combination
        """
        self.__param_combinations.append(param_combination)
        return self

    def add_param_combinations(self, param_combinations) -> TestStackBuilder:
        """
        Adds multiple param combinations at the same time.

        :param param_combinations: list of tuples containing a combination of
        values for the parameters of the target functions you are testing
        :return: a new TestStackBuilder with added parameter combinations
        """
        self.__param_combinations.extend(param_combinations)
        return self

    def repeat(self, n_times: int = 1000) -> TestStackBuilder:
        """
        Test should be repeated n times and results averaged
        :param n_times: the number of times to repeat test
        :return: a new TestStackBuilder with the repetitions altered
        """
        self.__repetitions = n_times
        return self

    def do_show_plot(self) -> TestStackBuilder:
        """
        Sets the output type for the tests.

        The output can be a graph (plot) or a data frame

        :param plot: true
        :return: a TestStackBuilder with plot set to the provided value
        """
        self.__plot = True
        return self

    def build(self) -> TestStack:
        """
        Builds a new TestStack with the specifications provided
        :return: a new TestStack with the specified characteristics
        """
        return TestStack(self)
