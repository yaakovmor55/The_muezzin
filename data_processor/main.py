from elastic_dal import ElasticDAL
from text_processing import TextProcessing
import config
from decryptor import decode_string

es = ElasticDAL()

for i,x in es.get_document().items():

    tp = TextProcessing(x, decode_string(config.HOSTILE_LIST), decode_string(config.LESS_HOSTILE_LIST))

    es.update(i,"bds_percent", tp.bds_percent())
    es.update(i,"is_bds", tp.bds_percent() > 49)
    es.update(i, "bds_threat_level", tp.get_bds_threat_level())
