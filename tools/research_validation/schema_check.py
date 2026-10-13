"""Offline validator for the JSON Schema subset used in this repository.

Supports object, array, primitive type, required, properties, additionalProperties,
enum, pattern, minLength, minimum and exclusiveMinimum. Rejects unsupported
validation keywords so a new schema cannot silently weaken these checks.
Not a replacement for a general Draft 2020-12 engine.
"""
import re

SUPPORTED = {'$schema','$id','title','description','type','properties','required',
             'additionalProperties','items','enum','pattern','minLength',
             'minimum','exclusiveMinimum'}

def validate(value, schema, path='$'):
    unknown = set(schema) - SUPPORTED
    if unknown:
        raise ValueError(f'{path}: unsupported schema keywords {sorted(unknown)}')
    expected = schema.get('type')
    checks = {'object': isinstance(value,dict), 'array': isinstance(value,list),
              'string': isinstance(value,str), 'boolean': isinstance(value,bool),
              'integer': isinstance(value,int) and not isinstance(value,bool),
              'number': isinstance(value,(int,float)) and not isinstance(value,bool)}
    if expected and not checks.get(expected,False):
        raise ValueError(f'{path}: expected {expected}')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f'{path}: value outside enum')
    if expected == 'object':
        missing = set(schema.get('required',[])) - value.keys()
        if missing:
            raise ValueError(f'{path}: missing {sorted(missing)}')
        props = schema.get('properties',{})
        if schema.get('additionalProperties') is False and set(value)-props.keys():
            raise ValueError(f'{path}: unknown properties {sorted(set(value)-props.keys())}')
        for key,item in value.items():
            if key in props:
                validate(item,props[key],f'{path}.{key}')
    elif expected == 'array':
        for index,item in enumerate(value):
            validate(item,schema['items'],f'{path}[{index}]')
    elif expected == 'string':
        if len(value) < schema.get('minLength',0):
            raise ValueError(f'{path}: string too short')
        if 'pattern' in schema and not re.search(schema['pattern'],value):
            raise ValueError(f'{path}: pattern mismatch')
    elif expected in ('integer','number'):
        if 'minimum' in schema and value < schema['minimum']:
            raise ValueError(f'{path}: below minimum')
        if 'exclusiveMinimum' in schema and value <= schema['exclusiveMinimum']:
            raise ValueError(f'{path}: below exclusive minimum')
