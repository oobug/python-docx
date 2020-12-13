from ..ns import qn
from ..xmlchemy import BaseOxmlElement, OxmlElement, ZeroOrMore, ZeroOrOne


class CT_Sdt(BaseOxmlElement):
    """
    ``<w:sdt>`` element, containing the properties and text for a
    structured document tag.
    """

    sdtPr = ZeroOrOne("w:sdtPr")
    sdtEndPr = ZeroOrOne("w:sdtEndPr")
    sdtContent = ZeroOrOne("w:sdtContent")


class CT_SdtPr(BaseOxmlElement):
    """
    ``<w:sdtPr>`` element, child of ``<w:sdt>``, holds child elements
    that define properties.
    """

    pass


class CT_SdtContent(BaseOxmlElement):
    """
    ``<w:sdtContent>`` element, child of ``<w:sdt>``, specifies the
    contents of a structured document tag.
    """

    r = ZeroOrMore("w:r")


'''
class ContentControl(object):
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }

    _xml = """\
    <w:sdt xmlns:w="{w}">
      <w:sdtPr>
        <w:rPr>
          <w:rFonts w:cs="Arial"/>
          <w:i/>
          <w:sz w:val="20"/>
          <w:szCs w:val="20"/>
          <w:lang w:val="en-CA"/>
        </w:rPr>
        <w:alias w:val=""/>
        <w:tag w:val=""/>
        <w:id w:val="718174177"/>
        <w:placeholder>
          <w:docPart w:val="E11F5001B9B44C169959B78BA4F1B1D7"/>
        </w:placeholder>
        <w:showingPlcHdr/>
      </w:sdtPr>
      <w:sdtEndPr/>
      <w:sdtContent>
        <w:r w:rsidR="00B43615" w:rsidRPr="005C43CE">
          <w:rPr>
            <w:rStyle w:val="PlaceholderText"/>
            <w:rFonts w:eastAsiaTheme="minorHAnsi"/>
            <w:i/>
            <w:sz w:val="18"/>
            <w:szCs w:val="18"/>
          </w:rPr>
          <w:t>Click here to enter text.</w:t>
        </w:r>
      </w:sdtContent>
    </w:sdt>""".format(**namespaces)

    _valattribute = '{{{0[w]}}}val'.format(namespaces)

    def __init__(self):
        self.element = etree.fromstring(self._xml)
        self._tagElement = self.element.xpath(
            'w:sdtPr/w:tag', namespaces=self.namespaces)[0]
        self._titleElement = self.element.xpath(
            'w:sdtPr/w:alias', namespaces=self.namespaces)[0]

    def _GetValueAttribute(self, element):
        return element.get(self._valattribute)

    def _SetValueAttribute(self, element, value):
        return element.set(self._valattribute, value)

    @property
    def tag(self):
        return self._GetValueAttribute(self._tagElement)

    @tag.setter
    def tag(self, value):
        self._SetValueAttribute(self._tagElement, value)

    @property
    def title(self):
        return self._GetValueAttribute(self._titleElement)

    @title.setter
    def title(self, value):
        self._SetValueAttribute(self._titleElement, value)
'''
