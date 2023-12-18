from typing import Any


def tagging(self):
    tag = self.tag
    return "<{tag}></{tag}>".format(tag=tag)


def attrs(self) -> str:
    attrskey = self.attrskey
    attrsvalue = self.attrsvalue
    tag = self.tag
    result = "{attrskey}='{attrsvalue}'".format(
        attrskey=attrskey, attrsvalue=attrsvalue
    )
    return result


def innerhtml(self) -> Any:
    innerhtml = self.innerhtml
    return innerhtml


def join(tag, attrskey, attrsvalue, innerhtml) -> str:
    result = "<{tag} {attrskey}='{attrsvalue}'>{innerhtml}</{tag}>".format(
        tag=tag, attrskey=attrskey, attrsvalue=attrsvalue, innerhtml=innerhtml
    )
    return result
