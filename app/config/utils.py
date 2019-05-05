from fnmatch import fnmatch


class global_ip_list(list):
    def __contains__(self, value):
        for pattern in self:
            if fnmatch(value, pattern):
                return True
        return False
