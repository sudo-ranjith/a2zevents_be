from app import app
import app.Common.helpers as common_helpers
import traceback
from app import mongo


class RegisterCurb:
    """
         This class insert data
         @author:
         @return: success or failure message
     """

    def insert_data(self, query):
        try:
            users = app.config.get('REGISTRATION_COL')
            register_col = mongo.db.users
            registered_email = register_col.insert_one(query)
           
        except Exception as e:
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

    def read_data(self, query):
        try:
            register_col = mongo.db.users
            result_data = register_col.find_one(query)
            print(result_data)
            if result_data:
                return {"exists": True, "item": result_data}
            return {"exists": False, "item": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)
