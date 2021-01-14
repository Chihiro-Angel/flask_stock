# -*- coding: utf-8 -*-
# author:yang  time:19-8-7 上午9:47


from . import db


class Stock(db.Model):

    __tablename__ = "info"

    id = db.Column(db.Integer, primary_key=True)                 # 序号
    stock_code = db.Column(db.String(10), nullable=False)        # 股票代码
    stock_name = db.Column(db.String(40), nullable=False)        # 股票简称
    applies = db.Column(db.String(10), nullable=False)           # 涨跌幅
    turnover_rate = db.Column(db.String(10), nullable=False)     # 换手率
    latest_price = db.Column(db.Float, nullable=False)           # 最新价
    previous_highs = db.Column(db.Float, nullable=False)         # 前期高点
    highs_data = db.Column(db.Date, nullable=False)              # 前期最高点日期

    def to_basic_dict(self):
        resp_dict = {
            'stock_code': self.stock_code,
            'stock_name': self.stock_name,
            'applies': self.applies,
            'turnover_rate': self.turnover_rate,
            'latest_price': self.latest_price,
            'previous_highs': self.previous_highs
        }
        return resp_dict

    def to_dict(self):
        resp_dict = {
            'id': self.id,
            'stock_code': self.stock_code,
            'stock_name': self.stock_name,
            'applies': self.applies,
            'turnover_rate': self.turnover_rate,
            'latest_price': self.latest_price,
            'previous_highs': self.previous_highs,
            'highs_data': self.highs_data
        }
        return resp_dict


class Focus(db.Model):

    __tablename__ = "focus"

    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(80), nullable=True, default='')
    relationship_id = db.Column(db.Integer, db.ForeignKey('info.id'))

    def to_dict(self):
        stocks = Stock.query.get(self.relationship_id).to_basic_dict()

        resp_dict = {
            'id': self.id,
            'note': self.note,
            'relationship_id': self.relationship_id,
            'relationship': stocks
        }
        return resp_dict
