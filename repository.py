from os import environ

from github_object import GithubObject


class Repository(GithubObject):
    ATTRIBUTES: tuple[str, str, str] = ('name', 'description', 'fork')
    GITHUB_API_OBJECT_NAME: str = 'repos'
