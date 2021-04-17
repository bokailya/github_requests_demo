from os import environ

from github_object import GithubObject


class Following(GithubObject):
    ATTRIBUTES: tuple[str, str, str] = ('login', )
    GITHUB_API_OBJECT_NAME: str = 'following'
