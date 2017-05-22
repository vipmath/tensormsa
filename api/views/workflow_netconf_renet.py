import json
from rest_framework.response import Response
from rest_framework.views import APIView
from master.workflow.netconf.workflow_netconf_renet import WorkFlowNetConfReNet
from master import models

class WorkFlowNetConfRenet(APIView) :
    """

    """
    def post(self, request, nnid, ver, node):
        """
        - desc : insert data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, nnid, ver, node):
        """
        - desc : get data
        """
        try:
            nodeid = ''.join([nnid, '_', ver , '_', node])
            return_data = WorkFlowNetConfReNet().get_view_obj(nodeid)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, nnid, ver, node):
        """
        - desc ; update data
        """
        try:
            input_data = request.data
            node_id = ''.join([nnid, '_', ver , '_', node])
            obj = models.NN_WF_NODE_INFO.objects.get(nn_wf_node_id=node_id)
            old_config_data = getattr(obj, 'node_config_data')
            input_data["labels"] = old_config_data["labels"]
            return_data = WorkFlowNetConfReNet().set_view_obj(node_id, input_data)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, nnid, ver, node):
        """
        - desc : delete  data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
