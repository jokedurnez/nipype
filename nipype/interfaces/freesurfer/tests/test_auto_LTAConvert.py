# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import LTAConvert


def test_LTAConvert_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_fsl=dict(argstr='--infsl %s',
    mandatory=True,
    xor=('in_lta', 'in_fsl', 'in_mni', 'in_reg', 'in_niftyreg', 'in_itk'),
    ),
    in_lta=dict(argstr='--inlta %s',
    mandatory=True,
    xor=('in_lta', 'in_fsl', 'in_mni', 'in_reg', 'in_niftyreg', 'in_itk'),
    ),
    in_mni=dict(argstr='--inmni %s',
    mandatory=True,
    xor=('in_lta', 'in_fsl', 'in_mni', 'in_reg', 'in_niftyreg', 'in_itk'),
    ),
    in_niftyreg=dict(argstr='--inniftyreg %s',
    mandatory=True,
    xor=('in_lta', 'in_fsl', 'in_mni', 'in_reg', 'in_niftyreg', 'in_itk'),
    ),
    in_reg=dict(argstr='--inreg %s',
    mandatory=True,
    xor=('in_lta', 'in_fsl', 'in_mni', 'in_reg', 'in_niftyreg', 'in_itk'),
    ),
    in_reg=dict(argstr='--initk %s',
    mandatory=True,
    xor=('in_lta', 'in_fsl', 'in_mni', 'in_reg', 'in_niftyreg', 'in_itk'),
    ),
    invert=dict(argstr='--invert',
    ),
    ltavox2vox=dict(argstr='--ltavox2vox',
    requires=['out_lta'],
    ),
    out_fsl=dict(argstr='--outfsl %s',
    ),
    out_lta=dict(argstr='--outlta %s',
    ),
    out_mni=dict(argstr='--outmni %s',
    ),
    out_reg=dict(argstr='--outreg %s',
    ),
    out_itk=dict(argstr='--outitk %s',
    ),
    source_file=dict(argstr='--src %s',
    ),
    target_conform=dict(argstr='--trgconform',
    ),
    target_file=dict(argstr='--trg %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = LTAConvert.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_LTAConvert_outputs():
    output_map = dict(out_fsl=dict(),
    out_lta=dict(),
    out_mni=dict(),
    out_reg=dict(),
    out_itk=dict(),
    )
    outputs = LTAConvert.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
