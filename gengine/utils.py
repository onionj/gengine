
class _UID:
    """Generate unique id"""
    __last_uid: int = 0

    @classmethod
    def get_uid(cls) -> int:
        uid = cls.__last_uid
        cls.__last_uid += 1
        return uid
