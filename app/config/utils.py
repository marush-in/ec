from fnmatch import fnmatch


class global_ip_list(list):
    def __contains__(self, value):
        for global_ip in self:
            if fnmatch(value, global_ip):
                return True
        return False
