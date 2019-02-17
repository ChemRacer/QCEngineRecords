import qcengine as qcng
inp = {
    "molecule": {
        "geometry": [
            0.0, 0.0, -0.1294769411935893, 0.0, -1.494187339479985,
            1.0274465079245698, 0.0, 1.494187339479985, 1.0274465079245698
        ],
        "symbols": ["O", "H", "H"],
        "connectivity": [[0, 1, 1], [0, 2, 1]]
    },
    "driver": "gradient",
    "keywords": {},
    "model": {
        "method": "HF",
        "basis": "sto-3g"
    }
}

import qcelemental as qcel

inp = qcel.models.ResultInput(**inp)
#print(inp)

config = qcng.get_config()
qcng.programs.molpro._format_input(inp, config)