from app import key_hash_generate


def test_key_hash_generate():
    assert key_hash_generate('kcndhfjk^865zd*a') == 'ca074f6f20d7b44b389c4d49c6c5c911d28f98d1050358f1c0649b3faae506fba304e8aacdb7655dac6559aa695af71ef85d1358277db4233d4da29d9e299c6a'
    assert key_hash_generate('8jsncu8anzbd&)(_') == '9fb15992c442e8eeae178a8c06cbb7e09eb47941d8c15d3474b4685b281de1c9ec88728ac34bdad1ab6df18f50e8ab6146d1521da99fcf85b008294927dcd5fc'
    assert key_hash_generate('as9q(&^!cs;____)') == 'd502b2357a323da10ed5c6d91aa9d8a5b7ae108674f0876aa21ee85e8f404feb0fd7d4008dbd9e0e998d0cd5ed21faae4aca4f5271c1ac4fd3a4b90017e74850'
    assert key_hash_generate('HAJHSmc((&_**^))') == '225a38c7901d1b7f566ff9cf6775dac52e93e841705c560dc3b4428641aae619e5a2c768d9f1fd3a1aa8e5a0834414d604898913479152443d8ac19ede79b2e0'
    assert key_hash_generate('Z__A(A^!33744_);') == 'f0cb5865809eb408ebb98ae15dec7a51ceeeee81f5948101655efc1b1168df9cf5eb89eb360670025b848c1a4b1df1b6f5a25120eeee9c435d871115f5feea75'
