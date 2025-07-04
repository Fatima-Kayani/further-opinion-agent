import scrapy

class DawaaiSpider(scrapy.Spider):
    name = "dawaai"
    allowed_domains = ["dawaai.pk"]
    start_urls = ["https://dawaai.pk/disease"]

    def parse(self, response):
        # find disease links with numeric ID at end
        for href in response.css("a::attr(href)").re(r"^/disease/.+/\d+"):
            yield response.follow(href, self.parse_disease)

    def parse_disease(self, response):
        title = response.css("h1::text").get(default="").strip()
        # each section under h6 headings with content until next heading or block
        sections = {}
        for header in ["Description", "Causes", "Risk factors", "Symptoms", "Diagnosis", "Management", "When to consult a doctor"]:
            items = response.xpath(
                f"//h6[contains(normalize-space(), '{header}')]/following-sibling::*"
            )
            text = ""
            for elem in items:
                if elem.root.tag in ["h6", "h5", "h4", "h3", "h2"]:
                    break
                text += " " + "".join(elem.xpath(".//text()").getall())
            sections[header.lower().replace(" ", "_")] = text.strip()

        yield {
            "url": response.url,
            "title": title,
            **sections
        }
