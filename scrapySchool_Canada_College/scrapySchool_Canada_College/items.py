# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyschoolCanadaCollegeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school_code = scrapy.Field()
    school_name = scrapy.Field()
    degree_level = scrapy.Field()
    location = scrapy.Field()
    campus = scrapy.Field()
    major_type1 = scrapy.Field()
    major_type2 = scrapy.Field()
    department = scrapy.Field()
    degree_name = scrapy.Field()
    degree_cname = scrapy.Field()
    degree_name_desc = scrapy.Field()
    major_name_en = scrapy.Field()
    major_name_cn = scrapy.Field()
    programme_code = scrapy.Field()
    overview_en = scrapy.Field()
    overview_cn = scrapy.Field()
    start_date = scrapy.Field()
    duration = scrapy.Field()
    duration_per = scrapy.Field()
    modules_en = scrapy.Field()
    modules_cn = scrapy.Field()
    career_en = scrapy.Field()
    career_cn = scrapy.Field()
    deadline = scrapy.Field()
    apply_pre = scrapy.Field()
    apply_fee = scrapy.Field()
    tuition_fee_pre = scrapy.Field()
    tuition_fee = scrapy.Field()
    tuition_fee_per = scrapy.Field()
    entry_requirements_en = scrapy.Field()
    entry_requirements_cn = scrapy.Field()
    require_chinese_en = scrapy.Field()
    require_chinese_cn = scrapy.Field()
    specific_requirement_en = scrapy.Field()
    specific_requirement_cn = scrapy.Field()
    average_score = scrapy.Field()
    current_state = scrapy.Field()
    gaokao_desc = scrapy.Field()
    gaokao_zs = scrapy.Field()
    huikao_desc = scrapy.Field()
    huikao_zs = scrapy.Field()
    ielts_desc = scrapy.Field()
    ielts = scrapy.Field()
    ielts_l = scrapy.Field()
    ielts_s = scrapy.Field()
    ielts_r = scrapy.Field()
    ielts_w = scrapy.Field()
    toefl_code = scrapy.Field()
    toefl_desc = scrapy.Field()
    toefl = scrapy.Field()
    toefl_l = scrapy.Field()
    toefl_s = scrapy.Field()
    toefl_r = scrapy.Field()
    toefl_w = scrapy.Field()
    interview_desc_en = scrapy.Field()
    interview_desc_cn = scrapy.Field()
    portfolio_desc_en = scrapy.Field()
    portfolio_desc_cn = scrapy.Field()
    other = scrapy.Field()
    url = scrapy.Field()
    gatherer = scrapy.Field()
    batch_number = scrapy.Field()
    update_time = scrapy.Field()