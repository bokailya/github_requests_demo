from __future__ import annotations
from abc import ABC
from os import environ
from typing import Any

from requests import get


class GithubObject(ABC):
    GITHUB_API_OBJECT_NAME: str = ''
    ATTRIBUTES: tuple[str, ...] = ()

    def __init__(self, json_data: dict[str, Any]) -> None:
        self.values: list[str] = [
            json_data[attribute] for attribute in self.ATTRIBUTES
        ]

    def __str__(self) -> str:
        return (
            '\n'.join(
                f"{attribute}: {value}"
                for attribute, value in zip(self.ATTRIBUTES, self.values)
            )
        )

    @classmethod
    def get_list(cls) -> list[GithubObject]:
        return [
            cls(json_data=json_object)
            for json_object in get(
                f"https://api.github.com/user/{cls.GITHUB_API_OBJECT_NAME}",
                auth=(environ['GITHUB_USERNAME'], environ['GITHUB_TOKEN']),
            ).json()
        ]
