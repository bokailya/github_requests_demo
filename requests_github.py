from json import dumps

from following import Following
from repository import Repository


def main():
    following = '\n\n'.join(map(str, Following.get_list()))
    repositories = '\n\n'.join(map(str, Repository.get_list()))
    print(
        f"""=== Repositories ===

{repositories}


=== Following ===

{following}
"""
    )


if __name__ == '__main__':
    main()
