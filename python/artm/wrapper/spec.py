"""
Specifications of C-API functions
"""

# TODO: generate this file automatically

import ctypes

import numpy

from . import messages_pb2 as messages


class CallSpec(object):
    def __init__(self, name, arguments, result=None, request=None):
        self.name = name
        self.arguments = arguments
        self.result_type = result
        self.request_type = request


ARTM_API = [

    CallSpec(
        'ArtmCreateMasterComponent',
        [('config', messages.MasterComponentConfig)],
        result=ctypes.c_int,
    ),
    CallSpec(
        'ArtmReconfigureMasterComponent',
        [('master_id', int), ('config', messages.MasterComponentConfig)],
    ),
    CallSpec(
        'ArtmDisposeMasterComponent',
        [('master_id', int)],
    ),

    ## deprecated
    #CallSpec(
    #    'ArtmCreateModel',
    #    [('master_id', int), ('config', messages.ModelConfig)],
    #),
    ## deprecated
    #CallSpec(
    #    'ArtmReconfigureModel',
    #    [('master_id', int), ('config', messages.ModelConfig)],
    #),
    CallSpec(
        'ArtmDisposeModel',
        [('master_id', int), ('name', str)],
    ),

    CallSpec(
        'ArtmCreateRegularizer',
        [('master_id', int), ('config', messages.RegularizerConfig)],
    ),
    CallSpec(
        'ArtmReconfigureRegularizer',
        [('master_id', int), ('config', messages.RegularizerConfig)],
    ),
    CallSpec(
        'ArtmDisposeRegularizer',
        [('master_id', int), ('name', str)],
    ),

    ## deprecated
    #CallSpec(
    #    'ArtmCreateDictionary',
    #    [('master_id', int), ('config', messages.DictionaryConfig)],
    #),
    ## deprecated
    #CallSpec(
    #    'ArtmReconfigureDictionary',
    #    [('master_id', int), ('config', messages.DictionaryConfig)],
    #),
    CallSpec(
        'ArtmDisposeDictionary',
        [('master_id', int), ('name', str)],
    ),
    CallSpec(
        'ArtmImportDictionary',
        [('master_id', int), ('args', messages.ImportDictionaryArgs)],
    ),
    CallSpec(
        'ArtmParseCollection',
        [('config', messages.CollectionParserConfig)],
    ),

    ## deprecated
    #CallSpec(
    #    'ArtmAddBatch',
    #    [('master_id', int), ('args', messages.AddBatchArgs)],
    #),
    ## deprecated
    #CallSpec(
    #    'ArtmInvokeIteration',
    #    [('master_id', int), ('args', messages.InvokeIterationArgs)],
    #),
    ## deprecated
    #CallSpec(
    #    'ArtmWaitIdle',
    #    [('master_id', int), ('args', messages.WaitIdleArgs)],
    #),
    ## deprecated
    #CallSpec(
    #    'ArtmSynchronizeModel',
    #    [('master_id', int), ('args', messages.SynchronizeModelArgs)],
    #),

    ## deprecated
    #CallSpec(
    #    'ArtmOverwriteTopicModel',
    #    [('master_id', int), ('model', messages.TopicModel)],
    #),
    CallSpec(
        'ArtmInitializeModel',
        [('master_id', int), ('args', messages.InitializeModelArgs)],
    ),
    CallSpec(
        'ArtmExportModel',
        [('master_id', int), ('args', messages.ExportModelArgs)],
    ),
    CallSpec(
        'ArtmImportModel',
        [('master_id', int), ('args', messages.ImportModelArgs)],
    ),
    CallSpec(
        'ArtmAttachModel',
        [('master_id', int), ('args', messages.AttachModelArgs), ('matrix', numpy.ndarray)],
    ),

    CallSpec(
        'ArtmRequestProcessBatches',
        [('master_id', int), ('args', messages.ProcessBatchesArgs)],
        request=messages.ProcessBatchesResult,
    ),
    CallSpec(
        'ArtmRequestProcessBatchesExternal',
        [('master_id', int), ('args', messages.ProcessBatchesArgs)],
        request=messages.ProcessBatchesResult,
    ),
    CallSpec(
        'ArtmMergeModel',
        [('master_id', int), ('args', messages.MergeModelArgs)],
    ),
    CallSpec(
        'ArtmRegularizeModel',
        [('master_id', int), ('args', messages.RegularizeModelArgs)],
    ),
    CallSpec(
        'ArtmNormalizeModel',
        [('master_id', int), ('args', messages.NormalizeModelArgs)],
    ),

    CallSpec(
        'ArtmRequestThetaMatrix',
        [('master_id', int), ('args', messages.GetThetaMatrixArgs)],
        request=messages.ThetaMatrix,
    ),
    CallSpec(
        'ArtmRequestThetaMatrixExternal',
        [('master_id', int), ('args', messages.GetThetaMatrixArgs)],
        request=messages.ThetaMatrix,
    ),
    CallSpec(
        'ArtmRequestTopicModel',
        [('master_id', int), ('args', messages.GetTopicModelArgs)],
        request=messages.TopicModel,
    ),
    CallSpec(
        'ArtmRequestTopicModelExternal',
        [('master_id', int), ('args', messages.GetTopicModelArgs)],
        request=messages.TopicModel,
    ),
    ## deprecated
    #CallSpec(
    #    'ArtmRequestRegularizerState',
    #    [('master_id', int), ('name', str)],
    #    request=messages.RegularizerInternalState,
    #),
    CallSpec(
        'ArtmRequestScore',
        [('master_id', int), ('args', messages.GetScoreValueArgs)],
        request=messages.ScoreData,
    ),
    CallSpec(
        'ArtmRequestParseCollection',
        [('args', messages.CollectionParserConfig)],
        request=messages.DictionaryConfig,
    ),
    CallSpec(
        'ArtmRequestLoadDictionary',
        [('filename', str)],
        request=messages.DictionaryConfig,
    ),
    CallSpec(
        'ArtmRequestLoadBatch',
        [('filename', str)],
        request=messages.Batch,
    ),

    CallSpec(
        'ArtmSaveBatch',
        [('filename', str), ('batch', messages.Batch)],
    ),

    CallSpec(
        'ArtmCopyRequestResultEx',
        [('args', messages.CopyRequestResultArgs), ('array', numpy.ndarray)],
    ),

]
