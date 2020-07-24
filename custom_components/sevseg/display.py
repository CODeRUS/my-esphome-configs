import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import display
from esphome.const import CONF_ID

sevseg_ns = cg.esphome_ns.namespace('sevseg')
SevSegComponent = sevseg_ns.class_('SevSeg', cg.Component)
SevSegComponentRef = SevSegComponent.operator('ref')

CONFIG_SCHEMA = display.BASIC_DISPLAY_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(SevSegComponent),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield display.register_display(var, config)
