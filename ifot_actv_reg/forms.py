from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, SubmitField
from wtforms.fields.html5 import DateField, TimeField, IntegerField
from wtforms.validators import DataRequired

INFLUX_IP_LIST  = [('IFoT-GW2', 'IFoT-GW2')]
MODEL_LIST      = [('all_k_neighbors__ActivityRecog.sav', 'all_k_neighbors__ActivityRecog.sav')]
SENSOR_LIST     = [('C259A61F7122', 'C259A61F7122'), 
                   ('C6BA89000DB6', 'C6BA89000DB6'), 
                   ('D718E3130C74', 'D718E3130C74'), 
                   ('EA747BD45226', 'EA747BD45226'),
                   ('F5E5D6FFACAB', 'F5E5D6FFACAB')] 
PARAM_LIST      = [('humidity', 'humidity'),
                   ('light', 'light'), 
                   ('noise', 'noise'), 
                   ('rssi', 'rssi'), 
                   ('temperature', 'temperature') ] 

class TrainForm(FlaskForm):
    influx_ip = SelectField( 'Influx IP: ', choices=INFLUX_IP_LIST,
                                            validators=[DataRequired()] )
    model = SelectField( 'Model: ', choices=MODEL_LIST, 
                                    validators=[DataRequired()])
    sensor_list = SelectMultipleField( 'Sensors: ', choices=SENSOR_LIST, 
                                                    validators=[DataRequired()])
    start_date = DateField( 'Start: ', validators=[DataRequired()])
    end_date = DateField( 'End: ', validators=[DataRequired()])
    start_time = TimeField( 'Start: ', validators=[DataRequired()])
    end_time = TimeField( 'End: ', validators=[DataRequired()])
    split_count = IntegerField( 'Split Count: ', validators=[DataRequired()])
    submit = SubmitField('Train')





