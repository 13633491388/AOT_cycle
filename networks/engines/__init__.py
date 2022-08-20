from networks.engines.aot_engine import AOTEngine, AOTInferEngine,AOTgcEngine


def build_engine(name, phase='train', **kwargs):
    if name == 'aotengine':
        if phase == 'train':
            return AOTEngine(**kwargs)
        elif phase == 'eval':
            return AOTInferEngine(**kwargs)
        else:
            return AOTgcEngine(**kwargs)
    else:
        raise NotImplementedError
