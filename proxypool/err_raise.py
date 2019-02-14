#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PoolEmptyError(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return repr('Pool is EMPTY!')

class ResourceDepletionError(Exception):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return repr('The proxy source is exhausted, please add new websites for more ip.')