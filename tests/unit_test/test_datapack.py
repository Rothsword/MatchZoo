from matchzoo.datapack import DataPack, load_datapack

import pytest
import shutil

import numpy as np

@pytest.fixture
def data_pack():
    data = np.zeros((2, 2))
    mapping = {'qid0': {'id_right': 'did0', 'label': 1}}
    ctx = {'vocab_size': 2000}
    return DataPack(data=data, mapping=mapping, context=ctx)

def test_length(data_pack):
    num_examples = 2
    assert len(data_pack) == num_examples

def test_mapping(data_pack):
    assert data_pack.mapping['qid0']['id_right'] == 'did0'

def test_save_load(data_pack):
    dirpath = '.tmpdir'
    data_pack.save(dirpath)
    dp = load_datapack(dirpath)
    with pytest.raises(FileExistsError):
        data_pack.save(dirpath)
    assert len(data_pack) == 2
    shutil.rmtree(dirpath)
