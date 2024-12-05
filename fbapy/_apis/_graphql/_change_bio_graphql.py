from ..._utils import DefaultFuncs, parse_and_check_login
import json
import base64

def change_bio_graphql(default_funcs: DefaultFuncs, ctx: dict):
    def change(bio_content: str, publish_bio: bool):
        data = f"profile_tile_view:{ctx['user_id']}:intro:intro_bio:intro_card_bio:profile_timeline:1"
        byte1 = data.encode('utf-8')
        enc1 = base64.b64encode(byte1)
        pvti = enc1.decode('utf-8')
        form = {
            "av": ctx["user_id"],
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "ProfileCometSetBioMutation",
            "doc_id": "6996613973732391",
            "variables": json.dumps(
                {
                    "input": {
                        "attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1733367271707,3800,190055527696468,,;CometHomeRoot.react,comet.home,via_cold_start,1733367247764,265762,4748854339,,",
                        "bio": bio_content,
                        "publish_bio_feed_story": publish_bio,
                        "actor_id": ctx["user_id"],
                        "client_mutation_id": "3",
                    },
                    "hasProfileTileViewID": True,
                    "profileTileViewID":pvti,
                    "scale": 1.5,
                    "useDefaultActor": False,
                }
            ),
        }

        res = default_funcs.post_with_defaults("https://www.facebook.com/api/graphql/", form, ctx)

        return parse_and_check_login(res, ctx, default_funcs)

    return change
