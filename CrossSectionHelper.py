from collections import namedtuple,Mapping

def namedtuple_with_defaults(typename, field_names, default_values=()):
    T = namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


class MCSampleValuesHelper():
    """Stores the cross sections and k-factors associated to a given physics process.

    The lists of years and energies used to identify a given cross section are also stored within this class.
    Given a process name, and year the appropriate cross section will be returned.

    Args:
        extra_dicts (:obj:`dict` of :obj:`dict` of :obj:`namedtuple_with_defaults`): Extra cross sections and k-factors to add to the __values_dict.

    Example:
        from CrossSectionHelper import *
        helper = MCSampleValuesHelper()
        helper.get_lumi("TTbarTo2L2Nu","13TeV","2018")
        helper.get_xs("TTbarTo2L2Nu","13TeV","2018")
        helper.get_nevt("TTbarTo2L2Nu","13TeV","2018")
        helper.get_br("TTbarTo2L2Nu","13TeV","2018")
        helper.get_xml("TTbar","13TeV","2016")
    """

    __years = ["UL16preVFP","UL16postVFP","UL17","UL18"]
    __energies = ["13TeV"]
    __xs_field_names = []
    __nevt_field_names = []
    __br_field_names = []
    __kfactor_field_names = []
    __corr_field_names = []
    __xml_field_names = []
    __key_field_map = {
        "CrossSection"   : ("XSec",-1.0),
        "NEvents"        : ("NEVT",-1.0),
        "BranchingRatio" : ("BRat",1.0),
        "kFactor"        : ("kFac",1.0),
        "Correction"     : ("Corr",1.0),
        "XMLname"        : ("Xml",""),
    }
    for __val in __years+__energies:
        for mode in ["", "Source"]:
            __xs_field_names.append("XSec"+mode+"_"+__val)
            __nevt_field_names.append("NEVT"+mode+"_"+__val)
            __br_field_names.append("BRat"+mode+"_"+__val)
            __kfactor_field_names.append("kFac"+mode+"_"+__val)
            __corr_field_names.append("Corr"+mode+"_"+__val)
            __xml_field_names.append("Xml"+mode+"_"+__val)
    XSValues      = namedtuple_with_defaults("XSValues",      __xs_field_names,       [__key_field_map["CrossSection"][1],""]*len(__years+__energies))
    NEventsValues = namedtuple_with_defaults("NEventsValues", __nevt_field_names,     [__key_field_map["NEvents"][1],""]*len(__years+__energies))
    BRValues      = namedtuple_with_defaults("BRValues",      __br_field_names,       [__key_field_map["BranchingRatio"][1],""]*len(__years+__energies))
    kFactorValues = namedtuple_with_defaults("kFactorValues", __kfactor_field_names,  [__key_field_map["kFactor"][1],""]*len(__years+__energies))
    CorrValues    = namedtuple_with_defaults("CorrValues",    __corr_field_names,     [__key_field_map["Correction"][1],""]*len(__years+__energies))
    XMLValues     = namedtuple_with_defaults("XMLValues",     __xml_field_names,      [__key_field_map["XMLname"][1],""]*len(__years+__energies))

    __values_dict = {

        "SingleMuon_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "SingleMuon_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2789243+158145722,
                NEVT_UL17=136300266,
                NEVT_UL18=119918017,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018B-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/SingleMuon/Run2018B-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=67441308,
                NEVT_UL17=165652756,
                NEVT_UL18=109986009,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018C-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/SingleMuon/Run2018C-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=98017996,
                NEVT_UL17=70361660,
                NEVT_UL18=513909894,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/SingleMuon_Run2018D-UL2018_MiniAODv2-v3.xml", XmlSource_UL18="/SingleMuon/Run2018D-UL2018_MiniAODv2-v3/MINIAOD",
            ),
        },

        "SingleMuon_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=90984718,
                NEVT_UL17=154618774,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=57465359,
                NEVT_UL16postVFP=8024195,
                NEVT_UL17=242140980,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleMuon_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data//SingleMuon_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleMuon_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleMuon_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=149916849,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleMuon_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=174035164,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleMuon_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleElectron_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1422819+246440440,
                NEVT_UL17=60537490,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016B_HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=97259854,
                NEVT_UL17=136637888,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=148167727,
                NEVT_UL17=51526521,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=117269446,
                NEVT_UL17=102122055,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016E-HIPM_UL2016_MiniAODv2-v5.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2-v5/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=61735326,
                NEVT_UL16postVFP=8858206,
                NEVT_UL17=128467223,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SingleElectron_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SingleElectron_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SingleElectron/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SingleElectron_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=153363109,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SingleElectron_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=129021893,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SingleElectron_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SingleElectron/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "SinglePhoton_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=13119462+56878553,
                NEVT_UL17=15950935,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=23147235,
                NEVT_UL17=42182948,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=29801360,
                NEVT_UL17=9753462,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=22322869,
                NEVT_UL17=19011446,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=12806145,
                NEVT_UL16postVFP=1860761,
                NEVT_UL17=29783015,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/SinglePhoton_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/SinglePhoton_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/SinglePhoton/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "SinglePhoton_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=33288854,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016G-UL2016_MiniAODv2-v3.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016G-UL2016_MiniAODv2-v3/MINIAOD",
            ),
        },

        "SinglePhoton_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=35035661,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/SinglePhoton_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/SinglePhoton/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "EGamma_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=339013231,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018A-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "EGamma_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL18=153792795,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018B-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "EGamma_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL18=147827904,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "EGamma_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL18=752524583,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/EGamma_Run2018D-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=171484635,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018A-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/JetHT/JetHT_Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9726665+133752091,
                NEVT_UL17=63043590,
                NEVT_UL18=78255208,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018B-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/JetHT/JetHT_Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=46495988,
                NEVT_UL17=96264601,
                NEVT_UL18=70027804,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/JetHT/JetHT_Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=73330042,
                NEVT_UL17=46145204,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="", XmlSource_UL18="",
            ),
        },

        "JetHT_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=69219288,
                NEVT_UL17=89630771,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=41564915,
                NEVT_UL16postVFP=6613811,
                NEVT_UL17=115429972,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=120745085,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=124054791,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunA": {
            "NEvents" : NEventsValues(
                NEVT_UL18=52759851,
            ),
            "XMLname" : XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018A-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/MET/Run2018A-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunB": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=583427+35987712,
                NEVT_UL17=51623474,
                NEVT_UL18=29713483,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018B-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/MET/Run2018B-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunC": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17381222,
                NEVT_UL17=115906496,
                NEVT_UL18=31237456,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018C-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/MET/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunD": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=20947429,
                NEVT_UL17=20075033,
                NEVT_UL18=160411782,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/MET_Run2018D-UL2018_MiniAODv2-v1.xml", XmlSource_UL18="/MET/Run2018D-UL2018_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunE": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=22348402,
                NEVT_UL17=71418865,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunF": {
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11936579,
                NEVT_UL16postVFP=1383250,
                NEVT_UL17=177521562,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/MET_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/MET/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/MET_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/MET/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "MET_RunG": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=26974131,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "MET_RunH": {
            "NEvents" : NEventsValues(
                NEVT_UL16postVFP=39773485,
            ),
            "XMLname" : XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/MET_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/MET/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "TTTo2L2Nu" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2704527656.31,
                NEVT_UL16postVFP=3146182352.62,
                NEVT_UL17=7695841652.46,
                NEVT_UL18=10528968536.7,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=39772305956.8,
                NEVT_UL16postVFP=43624104390.1,
                NEVT_UL17=1.06922359713e+11,
                NEVT_UL18=1.44128770259e+11,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=30637661153.8,
                NEVT_UL16postVFP=34334910058.7,
                NEVT_UL17=73994630561.7,
                NEVT_UL18=1.07748739105e+11,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_hdampDOWN" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1223965702.6,
                NEVT_UL16postVFP=1305254604.97,
                NEVT_UL17=2929943912.75,
                NEVT_UL18=4323628397.15,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_hdampDOWN" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=18249770082.9,
                NEVT_UL17=40416900003.0,
                NEVT_UL18=58140739277.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_hdampDOWN" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11601553106.6,
                NEVT_UL16postVFP=13097955883.4,
                NEVT_UL17=29913495414.4,
                NEVT_UL18=43787698273.3,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_hdampDOWN_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_hdampUP" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=1361059107.92,
                NEVT_UL17=2905584113.05,
                NEVT_UL18=3930878067.9,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_hdampUP" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17142541164.3,
                NEVT_UL16postVFP=18309172997.5,
                NEVT_UL17=40017266549.6,
                NEVT_UL18=60002115817.1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_hdampUP" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=13200254086.6,
                NEVT_UL17=31228727737.2,
                NEVT_UL18=43349104310.5,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_hdampUP_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_CR1" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="/TTTo2L2Nu_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_CR1" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic_CR1" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="/TTToHadronic_TuneCP5CR1_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_CR2" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1209778279.97,
                NEVT_UL16postVFP=1299119114.88,
                NEVT_UL17=3072219680.55,
                NEVT_UL18=4131775059.13,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5CR2_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_CR2" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=12530751795.3,
                NEVT_UL16postVFP=13150665656.7,
                NEVT_UL17=31341511293.6,
                NEVT_UL18=40134252735.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5CR2_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTToHadronic_CR2" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16948358553.1,
                NEVT_UL16postVFP=18864528471.5,
                NEVT_UL17=42705231787.4,
                NEVT_UL18=58707487112.6,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5CR2_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTToHadronic_TuneCP5CR2_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_erdON" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="/TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_erdON" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_erdON" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=-1,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="", XmlSource_UL18="/TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_TuneCP5down" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1224164110.83,
                NEVT_UL16postVFP=1324614555.14,
                NEVT_UL17=2835763505.61,
                NEVT_UL18=4320812892.96,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_TuneCP5down" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16776724056.4,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=40047980719.4,
                NEVT_UL18=57198370847.7,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_TuneCP5down" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=11934112109.7,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=30498725616.3,
                NEVT_UL18=43890851036.3,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToHadronic_CP5down_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5down_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5down_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTTo2L2Nu_TuneCP5up" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.105, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=3089320938.48,
                NEVT_UL18=4166003310.52,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTTo2L2Nu_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToSemiLeptonic_TuneCP5up" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.438, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=14002115305.3,
                NEVT_UL16postVFP=17450463976.7,
                NEVT_UL17=41805223200.5,
                NEVT_UL18=60018531229.9,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToSemiLeptonic_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTToHadronic_TuneCP5up" : {
            "CrossSection" : XSValues(XSec_13TeV=831.76, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.457, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=13137584217.8,
                NEVT_UL17=30221996666.9,
                NEVT_UL18=43103983319.8,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTToHadronic_CP5up_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTToHadronic_CP5up_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTToHadronic_CP5up_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TT_Mtt-700to1000" : {
            "CrossSection" : XSValues(XSec_13TeV=6.472e+01, XSecSource_13TeV="GenXSecAnalyzer (NLO) run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : CorrValues(Corr_13TeV=1.20965315498, CorrSource_13TeV="Scales to NNLO+NNLL x-section of TTTo2L2Nu/TTToSemiLeptonic/TTToHadronic. This correction factor should always be used"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15678094533.0,
                NEVT_UL16postVFP=22646592839.0,
                NEVT_UL17=24182708233.9,
                NEVT_UL18=20714868719.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TT_Mtt-700to1000_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TT_Mtt-1000toInf" : {
            "CrossSection" : XSValues(XSec_13TeV=1.644e+01, XSecSource_13TeV="GenXSecAnalyzer (NLO) run on UL17 (other years and also XSDB give similar results); accuracy: NLO"),
            "Correction" : CorrValues(Corr_13TeV=1.21062828535, CorrSource_13TeV="Scales to NNLO+NNLL x-section of TTTo2L2Nu/TTToSemiLeptonic/TTToHadronic. This correction factor should always be used"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15221498037.0,
                NEVT_UL16postVFP=15749293533.9,
                NEVT_UL17=14803424869.0,
                NEVT_UL18=15475388953.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TT_Mtt-1000toInf_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTZToLLNuNu_M-10_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.86, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=3*(0.0337+0.0667), BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1415599.92644,
                NEVT_UL16postVFP=1477923.21991,
                NEVT_UL17=3464156.46185,
                NEVT_UL18=4782962.66323,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTZToLLNuNu_M-10_CP5_amcatnlo-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "TTZToQQ_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.86, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.69911, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=3206904.47682,
                NEVT_UL16postVFP=2758738.86304,
                NEVT_UL17=7143394.7065,
                NEVT_UL18=10134247.2843,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTZToQQ_CP5_amcatnlo-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },
        
        "TTWJetsToLNu_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.55, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.3259, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=953960.422456,
                NEVT_UL16postVFP=1113150.39282,
                NEVT_UL17=2500272.10687,
                NEVT_UL18=3525043.5175,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTWJetsToLNu_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "TTWJetsToQQ_TuneCP5" : {
            "CrossSection" : XSValues(XSec_13TeV=0.55, XSecSource_13TeV="Phys. Rev. Lett. 113 (2014) 212001 [doi:10.1103/PhysRevLett.113.212001]"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.6741, BRatSource_13TeV="P.A. Zyla et al. (Particle Data Group), Prog. Theor. Exp. Phys. 2020, 083C01 (2020) and 2021 update"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=184218.52966,
                NEVT_UL16postVFP=209107.004822,
                NEVT_UL17=444333.97475,
                NEVT_UL18=656374.27724,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/TTWJetsToQQ_CP5_amcatnloFXFX-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=74624668.1199,
                NEVT_UL16postVFP=80821434.5381,
                NEVT_UL17=183284892.424,
                NEVT_UL18=258137404.807,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_inclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=74766341.164,
                NEVT_UL16postVFP=83024147.0626,
                NEVT_UL17=184446306.91,
                NEVT_UL18=251902154.492,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_inclusiveDecays_CP5_powheg-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ST_tW_top_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=106897142.991,
                NEVT_UL16postVFP=109290196.259,
                NEVT_UL17=276021555.615,
                NEVT_UL18=365675749.158,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_top_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_tW_antitop_5f_NoFullyHadronicDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=35.85, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.543, BRatSource_13TeV="https://pdg.lbl.gov/2020/reviews/rpp2020-rev-top-quark.pdf (page 2: dileptonic + semileptonic; tW has the same BRs as ttbar)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=103260113.113,
                NEVT_UL16postVFP=118799348.667,
                NEVT_UL17=274168362.629,
                NEVT_UL18=358102373.387,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_tW_antitop_5f_NoFullyHadronicDecays_CP5_powheg-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_t-channel_top_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=136.02, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5948135154.41,
                NEVT_UL16postVFP=6703801970.36,
                NEVT_UL17=13808000646.6,
                NEVT_UL18=19000619397.2,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_t-channel_top_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_t-channel_antitop_4f_InclusiveDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=80.95, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1983864432.65,
                NEVT_UL16postVFP=1957283183.22,
                NEVT_UL17=4471058679.95,
                NEVT_UL18=6128118195.12,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16APV_v3.xml", XmlSource_UL16preVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL16_v3.xml", XmlSource_UL16postVFP="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_t-channel_antitop_4f_InclusiveDecays_CP5_powheg-madspin-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ST_s-channel_4f_leptonDecays" : {
            "CrossSection" : XSValues(XSec_13TeV=10.32, XSecSource_13TeV="https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec"),
            "BranchingRatio" : BRValues(BRat_13TeV=0.326, BRatSource_13TeV="https://pdg.lbl.gov/2021/listings/rpp2021-list-w-boson.pdf (page 5, W->lnu times 3, rounded)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=19592486.3309,
                NEVT_UL16postVFP=19433132.1012,
                NEVT_UL17=49292566.8068,
                NEVT_UL18=68767081.0067,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ST_s-channel_4f_leptonDecays_CP5_amcatnlo-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WW" : {
            "CrossSection" : XSValues(
                XSec_13TeV=75.91, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=75.96,
                XSec_UL16postVFP=75.91,
                XSec_UL17=75.92,
                XSec_UL18=75.91,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15859130.7832,
                NEVT_UL16postVFP=15821137.255,
                NEVT_UL17=15634116.2001,
                NEVT_UL18=15679122.7141,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WW_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WW_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WW_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WW_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WZ" : {
            "CrossSection" : XSValues(
                XSec_13TeV=27.56, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=27.55,
                XSec_UL16postVFP=27.56,
                XSec_UL17=27.54,
                XSec_UL18=27.58,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7934000.0,
                NEVT_UL16postVFP=7584000.0,
                NEVT_UL17=7889000.0,
                NEVT_UL18=7940000.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WZ_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WZ_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WZ_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WZ_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZZ" : {
            "CrossSection" : XSValues(
                XSec_13TeV=12.13, XSecSource_13TeV="GenXSecAnalyzer (LO) for UL 16",
                XSec_UL16preVFP=12.12,
                XSec_UL16postVFP=12.13,
                XSec_UL17=12.14,
                XSec_UL18=12.13,
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1282000.0,
                NEVT_UL16postVFP=1151000.0,
                NEVT_UL17=2706000.0,
                NEVT_UL18=-1,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZZ_CP5_pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZZ_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZZ_CP5_pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/", XmlSource_UL18="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-70to100" : {
            "CrossSection" : XSValues(XSec_13TeV=140.1, XSecSource_13TeV="GenXSecAnalyzer"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6724232,
                NEVT_UL16postVFP=5893910,
                NEVT_UL17=12205958,
                NEVT_UL18=17004433,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-70to100_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-100to200" : {
            "CrossSection" : XSValues(XSec_13TeV=140.2, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=9570042,
                NEVT_UL16postVFP=8316351,
                NEVT_UL17=18955253,
                NEVT_UL18=26202328,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-100to200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-200to400" : {
            "CrossSection" : XSValues(XSec_13TeV=38.399, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.999, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.999, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5862631,
                NEVT_UL16postVFP=5653782,
                NEVT_UL17=12513057,
                NEVT_UL18=18455718,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-200to400_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-400to600" : {
            "CrossSection" : XSValues(XSec_13TeV=5.21278, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.990, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.990, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2716892,
                NEVT_UL16postVFP=2491416,
                NEVT_UL17=5543804,
                NEVT_UL18=8908406,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-400to600_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-600to800" : {
            "CrossSection" : XSValues(XSec_13TeV=1.26567, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.975, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.975, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2681650,
                NEVT_UL16postVFP=2299853,
                NEVT_UL17=5278417,
                NEVT_UL18=7035971,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-600to800_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-800to1200" : {
            "CrossSection" : XSValues(XSec_13TeV=0.5684304, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.907, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.907, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2411091,
                NEVT_UL16postVFP=2393976,
                NEVT_UL17=4506887,
                NEVT_UL18=6678036,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-800to1200_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-1200to2500" : {
            "CrossSection" : XSValues(XSec_13TeV=0.1331514, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=0.833, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=0.833, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2189664,
                NEVT_UL16postVFP=1970857,
                NEVT_UL17=4802716,
                NEVT_UL18=6166852,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-1200to2500_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "DYJetsToLL_M-50_HT-2500toInf" : {
            "CrossSection" : XSValues(XSec_13TeV=0.00297803565, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.2245, kFacSource_UL16preVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL16postVFP=1.2245, kFacSource_UL16postVFP="XSDB NNLO/LO=6077.22/4963",
                kFac_UL17=1.1374, kFacSource_UL17="XSDB NNLO/LO=6077.22/5343",
                kFac_UL18=1.1421, kFacSource_UL18="XSDB NNLO/LO=6077.22/5321",
            ),
            "Correction" : CorrValues(
                Corr_UL17=1.015, CorrSource_UL17="https://twiki.cern.ch/twiki/bin/viewauth/CMS/MCKnownIssues#WJetsToLNu_HT_and_DYJets_HT_LO_M",
                Corr_UL18=1.015, CorrSource_UL18="Same as 2017",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=721404,
                NEVT_UL16postVFP=696811,
                NEVT_UL17=1480047,
                NEVT_UL18=1978203,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/DYJetsToLL_M-50_HT-2500toInf_CP5_PSweights_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-70to100" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1271, XSecSource_13TeV="GenXSecAnalyzer on UL16postVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=16931765.0,
                NEVT_UL16postVFP=19439931.0,
                NEVT_UL17=44736228.0,
                NEVT_UL18=66569448.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-70To100_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-100to200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1253, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=21734530.0,
                NEVT_UL16postVFP=19753958.0,
                NEVT_UL17=47424468.0,
                NEVT_UL18=51541593.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-200to400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=335.9, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=17870845.0,
                NEVT_UL16postVFP=15067621.0,
                NEVT_UL17=42602407.0,
                NEVT_UL18=58331446.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-400to600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=45.21, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2467498.0,
                NEVT_UL16postVFP=2115509.0,
                NEVT_UL17=5468473.0,
                NEVT_UL18=7444030.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-600to800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=10.99, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2344130.0,
                NEVT_UL16postVFP=2251807.0,
                NEVT_UL17=5545298.0,
                NEVT_UL18=7718765.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-800to1200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=4.936, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2510487.0,
                NEVT_UL16postVFP=2132228.0,
                NEVT_UL17=5088483.0,
                NEVT_UL18=7306187.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-1200to2500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1.156, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2119975.0,
                NEVT_UL16postVFP=2090561.0,
                NEVT_UL17=4955636.0,
                NEVT_UL18=6481518.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToLNu_HT-2500toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=0.02623, XSecSource_13TeV="GenXSecAnalyzer on UL16preVFP",
            ),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.21, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.21, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.21, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.21, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=808649.0,
                NEVT_UL16postVFP=709514.0,
                NEVT_UL17=1185699.0,
                NEVT_UL18=2097648.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToLNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-100to200" : {
            "CrossSection" : XSValues(XSec_13TeV=266.6, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7784090,
                NEVT_UL16postVFP=7083216,
                NEVT_UL17=18983897,
                NEVT_UL18=28876062,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-100To200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-200to400" : {
            "CrossSection" : XSValues(XSec_13TeV=73.08, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7531529,
                NEVT_UL16postVFP=6814106,
                NEVT_UL17=17349597,
                NEVT_UL18=22749608,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-200To400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-400to600" : {
            "CrossSection" : XSValues(XSec_13TeV=9.932, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6632524,
                NEVT_UL16postVFP=6114046,
                NEVT_UL17=13963690,
                NEVT_UL18=19810491,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-400To600_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-600to800" : {
            "CrossSection" : XSValues(XSec_13TeV=2.407, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=2030858,
                NEVT_UL16postVFP=1881671,
                NEVT_UL17=4418971,
                NEVT_UL18=5968910,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-600To800_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-800to1200" : {
            "CrossSection" : XSValues(XSec_13TeV=1.078, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=703970,
                NEVT_UL16postVFP=633500,
                NEVT_UL17=1513585,
                NEVT_UL18=2129122,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-800To1200_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-1200to2500" : {
            "CrossSection" : XSValues(XSec_13TeV=0.2514, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=136393,
                NEVT_UL16postVFP=115609,
                NEVT_UL17=267125,
                NEVT_UL18=381695,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-1200To2500_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZJetsToNuNu_HT-2500toInf" : {
            "CrossSection" : XSValues(XSec_13TeV=0.005569, XSecSource_13TeV="GenXSecAnalyzer"),
            "kFactor" : kFactorValues(
                kFac_UL16preVFP=1.23, kFacSource_UL16preVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL16postVFP=1.23, kFacSource_UL16postVFP="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL17=1.23, kFacSource_UL17="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
                kFac_UL18=1.23, kFacSource_UL18="https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns",
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=111838,
                NEVT_UL16postVFP=110461,
                NEVT_UL17=176201,
                NEVT_UL18=268224,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToNuNu_HT-2500ToInf_CP5_madgraphMLM-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT200to400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=2565.301991, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=8000572.0,
                NEVT_UL16postVFP=7065076.0,
                NEVT_UL17=15968057.0,
                NEVT_UL18=14310025.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT400to600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=276.629780, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5144427.0,
                NEVT_UL16postVFP=4455853.0,
                NEVT_UL17=9927793.0,
                NEVT_UL18=9335298.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT600to800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=59.078057, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7644050.0,
                NEVT_UL16postVFP=6793578.0,
                NEVT_UL17=14667933.0,
                NEVT_UL18=13633226.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "WJetsToQQ_HT800toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=28.761363, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7606882.0,
                NEVT_UL16postVFP=6769101.0,
                NEVT_UL17=14722417.0,
                NEVT_UL18=13557328.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/WJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT200to400" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1010.200257, XSecSource_13TeV="GenXSecAnalyzer run on UL18"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=8753905.0,
                NEVT_UL16postVFP=7285673.0,
                NEVT_UL17=-1,
                NEVT_UL18=14738284.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-200to400_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT400to600" : {
            "CrossSection" : XSValues(
                XSec_13TeV=114.207953, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7709128.0,
                NEVT_UL16postVFP=-1,
                NEVT_UL17=14884962.0,
                NEVT_UL18=13930474.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="", XmlSource_UL16postVFP="",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-400to600_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT600to800" : {
            "CrossSection" : XSValues(
                XSec_13TeV=25.348623, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6116617.0,
                NEVT_UL16postVFP=5500386.0,
                NEVT_UL17=11702567.0,
                NEVT_UL18=12029507.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-600to800_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZJetsToQQ_HT800toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=12.914550, XSecSource_13TeV="GenXSecAnalyzer run on UL17"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=4388402.0,
                NEVT_UL17=9384525.0,
                NEVT_UL18=9681521.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/ZJetsToQQ_HT-800toInf_CP5_madgraphMLM-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-15To20_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=2.804e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=4530702.5042,
                NEVT_UL17=9021334.99026,
                NEVT_UL18=9354640.99415,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-20To30_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=2.525e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=30854055.9904,
                NEVT_UL17=-1,
                NEVT_UL18=60641468.4388,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-30To50_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=1.366e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=35474172.0,
                NEVT_UL17=-1,
                NEVT_UL18=58627984.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50To80_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=3.777e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=21491325.0,
                NEVT_UL17=40377957.0,
                NEVT_UL18=40022458.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80To120_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=8.862e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=22008310.1674,
                NEVT_UL17=45986550.6848,
                NEVT_UL18=45571985.8354,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120To170_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=2.118e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=19773251.4183,
                NEVT_UL17=39395152.0766,
                NEVT_UL18=39115540.5162,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170To300_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=7.015e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=34290911.0,
                NEVT_UL17=73071987.0,
                NEVT_UL18=71926577.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300To470_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=6.201e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=29908658.4042,
                NEVT_UL17=58692920.2804,
                NEVT_UL18=58949766.2915,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-470To600_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=5.908e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=19771535.0062,
                NEVT_UL17=39491905.0538,
                NEVT_UL18=38453444.9014,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-600To800_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=1.825e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=18763139.5706,
                NEVT_UL17=39321941.1416,
                NEVT_UL18=38412789.1215,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-800To1000_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=3.276e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=38921526.0,
                NEVT_UL17=78215559.0,
                NEVT_UL18=78942993.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-1000_MuEnrichedPt5" : {
            "CrossSection" : XSValues(XSec_13TeV=1.077e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=14243204.0,
                NEVT_UL17=27478273.0,
                NEVT_UL18=27427130.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-30to50_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=6.418e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4361931.0,
                NEVT_UL16postVFP=4351014.0,
                NEVT_UL17=8784542.0,
                NEVT_UL18=8574589.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50to80_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.987e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5440758.0,
                NEVT_UL16postVFP=5443934.0,
                NEVT_UL17=10210400.0,
                NEVT_UL18=10524400.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80to120_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=3.671e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4848176.90015,
                NEVT_UL16postVFP=4805600.8317,
                NEVT_UL17=9617412.94144,
                NEVT_UL18=9469962.10221,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120to170_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=6.661e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4852628.34648,
                NEVT_UL16postVFP=5007404.35617,
                NEVT_UL17=9904361.63759,
                NEVT_UL18=9678015.18575,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170to300_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.654e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1855461.0,
                NEVT_UL16postVFP=1861129.0,
                NEVT_UL17=3678200.0,
                NEVT_UL18=3714642.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300toInf_EMEnriched" : {
            "CrossSection" : XSValues(XSec_13TeV=1.100e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=1142775.0,
                NEVT_UL16postVFP=1138742.0,
                NEVT_UL17=2214934.0,
                NEVT_UL18=2215994.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_20to30_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=3.055e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7913585.84161,
                NEVT_UL16postVFP=7308537.32977,
                NEVT_UL17=14171713.7236,
                NEVT_UL18=14061668.0471,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_30to80_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=3.612e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7971435.43066,
                NEVT_UL16postVFP=7718567.59966,
                NEVT_UL17=15246295.0499,
                NEVT_UL18=15366710.0093,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_80to170_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=3.376e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7690702.0,
                NEVT_UL16postVFP=7882938.0,
                NEVT_UL17=15571255.0,
                NEVT_UL18=15186397.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_170to250_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=2.127e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=7343309.67453,
                NEVT_UL16postVFP=7864034.40369,
                NEVT_UL17=15503825.881,
                NEVT_UL18=15736781.2064,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_Pt_250toInf_bcToE" : {
            "CrossSection" : XSValues(XSec_13TeV=5.634e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=6856820.0,
                NEVT_UL16postVFP=8152626.0,
                NEVT_UL17=15557421.0,
                NEVT_UL18=15767690.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL17_v3.xml", XmlSource_UL17="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_HT50to100" : {
            "CrossSection" : XSValues(
                XSec_13TeV=185900000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=36599034.0,
                NEVT_UL16postVFP=11197186.0,
                NEVT_UL17=26243010.0,
                NEVT_UL18=38599389.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT50to100_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT100to200" : {
            "CrossSection" : XSValues(
                XSec_13TeV=23610000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=67431856.0,
                NEVT_UL16postVFP=73506112.0,
                NEVT_UL17=54760426.0,
                NEVT_UL18=84461486.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT200to300" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1551000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=18273591.0,
                NEVT_UL16postVFP=43280518.0,
                NEVT_UL17=42714435.0,
                NEVT_UL18=57336623.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT200to300_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT300to500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=324300, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46863466.0,
                NEVT_UL17=43589739.0,
                NEVT_UL18=61705174.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT300to500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT500to700" : {
            "CrossSection" : XSValues(
                XSec_13TeV=30340, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=56868784.0,
                NEVT_UL16postVFP=15222746.0,
                NEVT_UL17=36194860.0,
                NEVT_UL18=49184771.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT500to700_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT700to1000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=6440, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=15808790.0,
                NEVT_UL16postVFP=13905714.0,
                NEVT_UL17=34051754.0,
                NEVT_UL18=48506751.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_HT1000to1500" : {
            "CrossSection" : XSValues(
                XSec_13TeV=1118, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=13823774.0,
                NEVT_UL16postVFP=12675816.0,
                NEVT_UL17=10256089.0,
                NEVT_UL18=14527915.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT1500to2000" : {
            "CrossSection" : XSValues(
                XSec_13TeV=108, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=10031077.0,
                NEVT_UL16postVFP=9376965.0,
                NEVT_UL17=7701876.0,
                NEVT_UL18=10871473.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT2000toInf" : {
            "CrossSection" : XSValues(
                XSec_13TeV=22, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=4996082.0,
                NEVT_UL16postVFP=4867995.0,
                NEVT_UL17=4112573.0,
                NEVT_UL18=5374711.0,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZlepHinc-600": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-800": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1200": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1400": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1600": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=93000,
                    NEVT_UL18=98000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-1800": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-2000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-2500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-3000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=99000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-3500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-4000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=97000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-4500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-5000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-5500": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=44000,
                    NEVT_UL17=97000,
                    NEVT_UL18=94000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-6000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=45000,
                    NEVT_UL17=100000,
                    NEVT_UL18=100000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-7000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=100000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

        "ZprimeToZHToZlepHinc-8000": {
                "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
                "NEvents" : NEventsValues(
                    NEVT_UL16preVFP=-1,
                    NEVT_UL16postVFP=46000,
                    NEVT_UL17=97000,
                    NEVT_UL18=97000,
                ),
                "XMLname" : XMLValues(
                    Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                    Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                    Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                    Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZlepHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZlepHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
                ),
            },

    "ZprimeToZHToZinvHinc-600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
            Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP=    "ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=91000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=98000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1200": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1200_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1200_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1400": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1400_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1400_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1600": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1600_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1600_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-1800": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=96000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-1800_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-1800_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-2000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-2000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-2000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-2500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=97000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-2500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-2500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-3000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-3000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-3000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-3500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=44000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-3500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-3500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-4000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-4000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-4000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-4500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-4500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-4500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-5000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-5000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-5000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-5500": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-5500_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-5500_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-6000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-6000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-6000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-7000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=97000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-7000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-7000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ZprimeToZHToZinvHinc-8000": {
            "CrossSection" : XSValues( XSec_13TeV=1, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=46000,
                NEVT_UL17=100000,
                NEVT_UL18=100000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ZprimeToZHToZinvHinc_narrow_M-8000_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ZprimeToZHToZinvHinc_narrow_M-8000_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ALP_ttbar_signal": {
            "CrossSection" : XSValues( XSec_13TeV=7.048, XSecSource_13TeV="XSDB (LO)"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5380000,
                NEVT_UL16postVFP=4600000,
                NEVT_UL17=9970000,
                NEVT_UL18=9733000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ALP_ttbar_signal_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ALP_ttbar_signal_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "ALP_ttbar_interference": {
            "CrossSection" : XSValues( XSec_13TeV=-28.248020, XSecSource_13TeV="GenXSecAnalyzer run on UL18"),
            "NEvents" : NEventsValues(
                NEVT_UL16preVFP=5399000,
                NEVT_UL16postVFP=4572000,
                NEVT_UL17=10000000,
                NEVT_UL18=9960000,
            ),
            "XMLname" : XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/BSM/UL16preVFP/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/BSM/UL16postVFP/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/BSM/UL17/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/BSM/UL18/ALP_ttbar_interference_CP5_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/ALP_ttbar_interference_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

    }

    def __init__(self, extra_dicts=None):

        if extra_dicts is not None:
            if type(extra_dicts) == dict:
                self.__values_dict.update(extra_dicts)
            elif type(extra_dicts) == list:
                for ed in extra_dicts:
                    self.__values_dict.update(ed)

    def get_value(self, name, energy, year, key, strict=False):
        """Return the value for a given MC sample, energy or year, and information type

        If information is stored for both an energy and a year, the value for the given energy will be preferentially returned.
        If strict checking is turned on the function will raise an error if a given dictionary or piece of information isn't found.
          Otherwise the default value will be returned with no error (i.e. will return 1.0 for kFactors)

        Args:
            name (`str`): The process name for a given MC sample
            energy (`str`): The simulated energy used during production of the MC sample
            year (`str`): The production year of the MC sample
            key (`str`): The type of information being requested. The Options can be found in the __key_field_map.
            strict (`bool`): Whether or not to perform strict checking of the dictionary

        """
        fields = [self.__key_field_map[key][0]+"_"+energy,self.__key_field_map[key][0]+"_"+year]
        if not name in self.__values_dict:
            raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + str(name) + "\"")
        if not key in self.__values_dict[name]:
            if strict:
                print(self.__values_dict[name])
                raise KeyError("ERROR MCSampleValuesHelper::The process \"" + str(name) + "\" does not contain a " + str(key) + " tuple")
            else:
                return self.__key_field_map[key][1]
        if not any(f in self.__values_dict[name][key]._fields for f in fields):
            if strict:
                print(self.__values_dict[name][key])
                raise KeyError("ERROR MCSampleValuesHelper::The " + str(key) + " tuple for process \"" + str(name) + "\" does contain the key(s) \"" + str(fields) + "\"")
            else:
                self.__key_field_map[key][1]

        if self.__values_dict[name][key].__getattribute__(fields[0]) != self.__key_field_map[key][1]:
            return self.__values_dict[name][key].__getattribute__(fields[0])
        else:
            return self.__values_dict[name][key].__getattribute__(fields[1])

    def get_xs(self, name, energy, year):
        return self.get_value(name, energy, year, "CrossSection", True)

    def get_nevt(self, name, energy, year):
        return self.get_value(name, energy, year, "NEvents", True)

    def get_br(self, name, energy, year):
        return self.get_value(name, energy, year, "BranchingRatio", False)

    def get_kfactor(self, name, energy, year):
        return self.get_value(name, energy, year, "kFactor", False)

    def get_corr(self, name, energy, year):
        return self.get_value(name, energy, year, "Correction", False)

    def get_xml(self, name, energy, year):
        return self.get_value(name, energy, year, "XMLname", False)

    def get_lumi(self, name, energy, year, kFactor=False, Corrections=False):
        xsec = self.get_xs(name, energy, year)
        xsec *= self.get_br(name, energy, year)
        if kFactor: xsec *= self.get_kfactor(name, energy, year)
        if Corrections: xsec *= self.get_corr(name, energy, year)
        return self.get_nevt(name, energy, year)/xsec

def print_database():
    helper = MCSampleValuesHelper()
    samples = list(MCSampleValuesHelper.__dict__["_MCSampleValuesHelper__values_dict"].keys())
    samples.sort()
    energies = MCSampleValuesHelper.__dict__["_MCSampleValuesHelper__energies"]
    years = MCSampleValuesHelper.__dict__["_MCSampleValuesHelper__years"]
    import re
    run_pattern = re.compile("(?P<run>(Run)+[ABCDEFGH]{1})")

    max_sample_length = max(len(s) for s in samples)

    def banner(text, decorator = "#", line_width = 30):
        print("")
        print(decorator*line_width)
        print("{text:{deco}^{width}s}".format(text=text,deco=decorator,width=line_width))
        print(decorator*line_width)
        print("")

    for energy in energies:
        banner(energy)
        for year in years:
            banner(year)
            for sample in samples:
                run_match = run_pattern.search(sample)
                isData = run_match is not None
                nevt = helper.get_nevt(sample,energy,year)
                lumi = "/" if (isData or nevt<0) else "%10.2g"%helper.get_lumi(sample,energy,year)
                nevt = "%10.2g"%nevt
                print('{sample: <{width}}-> nevt:{nevt: >5}, lumi:{lumi: >5}'.format(sample=sample, width=max_sample_length+3, nevt=nevt, lumi=lumi))
    return 0


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser(description="CrossSectionHelper Database: find and calculate crucial information for your Analysis!")

    parser.add_argument("--print", action="store_true", help="print number of events and calculated luminosity of all samples in database (This is primarily to test the integrety of the database).")

    args = parser.parse_args()

    if(args.print):
        print_database()
