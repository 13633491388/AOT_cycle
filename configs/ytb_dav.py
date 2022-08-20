import os
from .default import DefaultEngineConfig


class EngineConfig(DefaultEngineConfig):
    def __init__(self, exp_name='default', model='AOTT'):
        super().__init__(exp_name, model)
        
        self.init_dir()
        self.STAGE_NAME = 'YTB_DAV'
        self.PRETRAIN_FULL = True
        self.DATASETS = ['youtubevos', 'davis2017']
