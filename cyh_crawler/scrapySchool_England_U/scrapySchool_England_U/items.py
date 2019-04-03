# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyschoolEnglandItem(scrapy.Item):
    university = scrapy.Field()
    location = scrapy.Field()
    major_type1 = scrapy.Field()
    ucascode = scrapy.Field()
    ib = scrapy.Field()
    alevel = scrapy.Field()
    department = scrapy.Field()
    programme_en = scrapy.Field()
    degree_type = scrapy.Field()
    degree_name = scrapy.Field()
    start_date = scrapy.Field()
    overview_en = scrapy.Field()
    teach_time = scrapy.Field()
    teach_type = scrapy.Field()
    duration = scrapy.Field()
    duration_per = scrapy.Field()
    modules_en = scrapy.Field()
    assessment_en = scrapy.Field()
    career_en = scrapy.Field()
    tuition_fee_pre = scrapy.Field()
    tuition_fee = scrapy.Field()
    require_chinese_en = scrapy.Field()
    require_chinese_school_en = scrapy.Field()
    rntry_requirements = scrapy.Field()
    degree_requirements = scrapy.Field()
    major_requirements = scrapy.Field()
    professional_background = scrapy.Field()
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
    gre = scrapy.Field()
    gmat = scrapy.Field()
    gre_sub = scrapy.Field()
    lsat = scrapy.Field()
    mcat = scrapy.Field()
    work_experience_desc_en = scrapy.Field()
    application_open_date = scrapy.Field()
    deadline = scrapy.Field()
    apply_pre = scrapy.Field()
    apply_fee = scrapy.Field()
    interview_desc_en = scrapy.Field()
    portfolio_desc_en = scrapy.Field()
    apply_desc_en = scrapy.Field()
    apply_documents_en = scrapy.Field()
    apply_proces_en = scrapy.Field()
    other = scrapy.Field()
    url = scrapy.Field()
    gatherer = scrapy.Field()
    batch_number = scrapy.Field()
    # create_time = scrapy.Field()
    update_time = scrapy.Field()