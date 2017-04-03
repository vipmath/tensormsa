from master import models

class WorkFlowEvalConfig:
    def put_step_source(self, nnid, wfver, node, config_data):
        """
        putter for source step
        :param obj: config data from view
        :return:boolean
        """

        try:
            obj = models.NN_WF_NODE_INFO.objects.get(wf_state_id=str(nnid) + "_" + str(wfver), nn_wf_node_name=node)
            setattr(obj, 'node_config_data', config_data)
            obj.save()
            return config_data

        except Exception as e:
            raise Exception(e)

    def get_step_source(self, node_id):
        """
        putter for source step
        :param obj: config data from view
        :return:boolean
        """

        try:
            obj = models.NN_WF_NODE_INFO.objects.get(nn_wf_node_id=node_id)
            config_data = getattr(obj, 'node_config_data')
            return config_data

        except Exception as e:
            raise Exception(e)