"""hoyai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from api import views as rest_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # (?P<target>.*) : etl, master, cluster  , (?P<type>.*) : local, s3, rdb, etc
    url(r'^api/v1/type/server/target/(?P<target>.*)/type/(?P<type>.*)/',
        csrf_exempt(rest_view.ConfServerData.as_view())),

    # net definition manager
    url(r'^api/v1/type/common/target/nninfo/(?P<nnid>.*)/version/',
        csrf_exempt(rest_view.CommonNNInfoVersion.as_view())),
    url(r'^api/v1/type/common/target/nninfo/',
        csrf_exempt(rest_view.CommonNNInfoList.as_view())),

    # rule management
    url(r'^api/v1/type/rule/target/cate/',
        csrf_exempt(rest_view.CommonNNInfoList.as_view())),
    url(r'^api/v1/type/rule/target/cate/(?P<cate>.*)/subcate/',
        csrf_exempt(rest_view.CommonNNInfoList.as_view())),

    # workflow init
    url(r'^api/v1/type/wf/target/init/mode/simple/(?P<nnid>.*)/wfver/(?P<wfver>.*)/',
        csrf_exempt(rest_view.WorkFlowInitSimple.as_view())),
    url(r'^api/v1/type/wf/target/init/mode/easy/(?P<nnid>.*)/',
        csrf_exempt(rest_view.WorkFlowInitEasy.as_view())),
    url(r'^api/v1/type/wf/target/init/mode/custom/(?P<nnid>.*)/',
        csrf_exempt(rest_view.WorkFlowInitCustom.as_view())),
    url(r'^api/v1/type/wf/target/init/mode/history/(?P<nnid>.*)/active/(?P<ver>.*)/',
        csrf_exempt(rest_view.WorkFlowInitHistory.as_view())),
    url(r'^api/v1/type/wf/target/init/mode/history/(?P<nnid>.*)/',
        csrf_exempt(rest_view.WorkFlowInitHistory.as_view())),
    url(r'^api/v1/type/wf/target/state/nnid/(?P<nnid>.*)/wfver/(?P<wfver>.*)/',
        csrf_exempt(rest_view.WorkFlowStateManager.as_view())),
    url(r'^api/v1/type/wf/target/node/nnid/(?P<nnid>.*)/wfver/(?P<wfver>.*)/',
        csrf_exempt(rest_view.WorkFlowNodeManager.as_view())),
    url(r'^api/v1/type/wf/target/menu/(?P<menu>.*)/submenu/',
        csrf_exempt(rest_view.WorkFlowSubMenuManager.as_view())),
    url(r'^api/v1/type/wf/target/menu/',
        csrf_exempt(rest_view.WorkFlowMenuManager.as_view())),

    # workflow - data APIs
    # 1.(?P<src>.*) : localcsv, s3, hbase, rdb, etc.. , 2.(?P<format>.*) : default  3. (?P<prg>.*) : source, pre, store
    url(r'^api/v1/type/wf/state/imgdata/src/(?P<src>.*)/form/(?P<form>.*)/prg/(?P<prg>.*)/nnid/(?P<nnid>.*)/ver/'
        r'(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowDataImage.as_view())),

    # 1.(?P<src>.*) : localcsv, s3, hbase, rdb, etc.. , 2.(?P<format>.*) : default  3. (?P<prg>.*) : source, pre, store
    url(r'^api/v1/type/wf/state/framedata/src/(?P<src>.*)/form/(?P<form>.*)/prg/(?P<prg>.*)/nnid/(?P<nnid>.*)/ver/'
        r'(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowDataFrame.as_view())),

    # 1.(?P<src>.*) : local, s3, hbase, etc.. , 2.(?P<format>.*) : file, line, tag, raw, default  3. (?P<prg>.*) : source, pre, store
    url(r'^api/v1/type/wf/state/textdata/src/(?P<src>.*)/form/(?P<form>.*)/prg/(?P<prg>.*)/nnid/(?P<nnid>.*)/ver/'
        r'(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowDataText.as_view())),

    url(r'^api/v1/type/wf/state/data/detail/reuse/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowDataReuse.as_view())),

    # workflow - data config APIs
    url(r'^api/v1/type/wf/state/dataconf/detail/frame/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowDataConfFrame.as_view())),
    url(r'^api/v1/type/wf/state/dataconf/detail/image/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowDataConfImage.as_view())),

    # workflow - preprocess APIs
    url(r'^api/v1/type/wf/state/pre/detail/predict/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowPrePredict.as_view())),
    url(r'^api/v1/type/wf/state/pre/detail/merge/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowPreMerge.as_view())),

    # workflow - net config APIs
    url(r'^api/v1/type/wf/state/netconf/detail/autoencoder/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfAutoEncoder.as_view())),
    url(r'^api/v1/type/wf/state/netconf/detail/cnn/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfCnn.as_view())),
    url(r'^api/v1/type/wf/state/netconf/detail/gru/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfGru.as_view())),
    url(r'^api/v1/type/wf/state/netconf/detail/lstm/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfLstm.as_view())),
    url(r'^api/v1/type/wf/state/netconf/detail/predefined/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfPredefined.as_view())),
    url(r'^api/v1/type/wf/state/netconf/detail/rnn/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfRnn.as_view())),
    url(r'^api/v1/type/wf/state/netconf/detail/wdnn/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfWdnn.as_view())),
    url(r'^api/v1/type/wf/state/netconf/detail/w2v/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.WorkFlowNetConfW2V.as_view())),

    # workflow - test APIs
    url(r'^api/v1/type/wf/state/test/nnid/{nnid}/ver/{ver}/',
        csrf_exempt(rest_view.WorkFlowTestConf.as_view())),

    # runmanager
    url(r'^api/v1/type/runmanager/state/schedule/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/',
        csrf_exempt(rest_view.RunManagerSchedule.as_view())),
    url(r'^api/v1/type/runmanager/state/workflow/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/',
        csrf_exempt(rest_view.RunManagerWorkFlow.as_view())),
    url(r'^api/v1/type/runmanager/state/history/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/',
        csrf_exempt(rest_view.RunManagerHistory.as_view())),
    url(r'^api/v1/type/runmanager/state/train/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/node/(?P<node>.*)/',
        csrf_exempt(rest_view.RunManagerSingleRequest.as_view())),
    url(r'^api/v1/type/runmanager/state/train/nnid/(?P<nnid>.*)/ver/(?P<ver>.*)/',
        csrf_exempt(rest_view.RunManagerTrainRequest.as_view())),

    # summary
    url(r'^api/v1/type/result/nnid/{nnid}/ver/{ver}/',
        csrf_exempt(rest_view.ResultManagerDefault.as_view())),

    # service
    url(r'^api/v1/type/wf/target/init/mode/history/(?P<nnid>.*)/ver/(?P<ver>.*)/batch//(?P<bver>.*)/',
        csrf_exempt(rest_view.ServiceManager.as_view())),
    url(r'^api/v1/type/service/state/predict/type/(?P<type>.*)/nnid/(?P<nnid>.*)/',
        csrf_exempt(rest_view.ServiceManagerPredict.as_view())),
]
