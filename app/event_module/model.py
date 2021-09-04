from app import app
import app.Common.helpers as common_helpers
import traceback
from app import mongo
from pymongo import ReturnDocument


class RegisterCurb:
    """
         This class insert data
         @author:
         @return: success or failure message
     """
    
    def __init__(self):
        # assigning collection name here
        self.transport_agent_col = mongo.db.event_module
        

    def insert_data(self, query):
        try:
            registered_email = self.transport_agent_col.insert_one(query)
            
        except Exception as e:
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

    def get_count(self):
        try:
            user_info = self.transport_agent_col.find({})
            user_info = list(user_info)
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return {"data": user_info, "count": len(user_info)}
            
        except Exception as e:
            more_info = "Unable to Inserted data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)


    def read_all_data(self, query):
        try:
            result_data = self.transport_agent_col.find(query)
            print(result_data)
            if result_data:
                return {"exists": True, "data": list(result_data)}
            return {"exists": False, "data": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)
    def read_data(self, query):
        try:
            result_data = self.transport_agent_col.find_one(query)
            print(result_data)
            if result_data:
                return {"exists": True, "data": result_data}
            return {"exists": False, "data": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)

    def find_modify(self, query, update):
        try:
            result_data = self.transport_agent_col.find_one_and_update(query,{'$set':update}, return_document = ReturnDocument.AFTER)
            print(result_data)
            if result_data:
                return {"exists": True, "data": result_data}
            return {"exists": False, "data": result_data}

        except Exception as e:
            more_info = "Unable to fetch data : Exception occurred - " + traceback.format_exc()
            return common_helpers.response('failed',
                                           app.config["FAILURE_MESSAGE_500"],
                                           more_info, [], 500)
