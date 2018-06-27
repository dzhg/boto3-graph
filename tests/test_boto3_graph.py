
from boto3_graph.cli import main


def test_main():
    assert main([]) == 0
