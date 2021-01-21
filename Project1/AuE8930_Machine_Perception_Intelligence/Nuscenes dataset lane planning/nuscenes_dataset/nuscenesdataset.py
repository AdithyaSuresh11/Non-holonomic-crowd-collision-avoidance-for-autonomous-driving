import matplotlib.pyplot as plotter
from nuscenes.nuscenes import NuScenes
from nuscenes.utils.data_classes import RadarPointCloud

nusc = NuScenes(version='v1.0-mini', dataroot='E:/data/sets/nuscenes', verbose=True)

nusc.list_scenes()
my_scene = nusc.scene[0]
my_scene
first_sample_token = my_scene['first_sample_token']

# The rendering command below is commented out because it tends to crash in notebooks
# nusc.render_sample(first_sample_token)
my_sample = nusc.get('sample', first_sample_token)
my_sample
nusc.list_sample(my_sample['token'])

my_sample['data']

sensor = 'CAM_FRONT'
cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])
cam_front_data

nusc.render_sample_data(cam_front_data['token'])

my_annotation_token = my_sample['anns'][18]
my_annotation_metadata =  nusc.get('sample_annotation', my_annotation_token)
my_annotation_metadata

nusc.render_annotation(my_annotation_token)

my_instance = nusc.instance[599]
my_instance

instance_token = my_instance['token']
nusc.render_instance(instance_token)

print("First annotated sample of this instance:")
nusc.render_annotation(my_instance['first_annotation_token'])
print("Last annotated sample of this instance")
nusc.render_annotation(my_instance['last_annotation_token'])

nusc.list_categories()
nusc.category[9]

nusc.list_attributes()

my_instance = nusc.instance[27]
first_token = my_instance['first_annotation_token']
last_token = my_instance['last_annotation_token']
nbr_samples = my_instance['nbr_annotations']
current_token = first_token

i = 0
found_change = False
while current_token != last_token:
    current_ann = nusc.get('sample_annotation', current_token)
    current_attr = nusc.get('attribute', current_ann['attribute_tokens'][0])['name']

    if i == 0:
        pass
    elif current_attr != last_attr:
        print("Changed from `{}` to `{}` at timestamp {} out of {} annotated timestamps".format(last_attr, current_attr, i, nbr_samples))
        found_change = True

    next_token = current_ann['next']
    current_token = next_token
    last_attr = current_attr
    i += 1

nusc.visibility
anntoken = 'a7d0722bce164f88adf03ada491ea0ba'
visibility_token = nusc.get('sample_annotation', anntoken)['visibility_token']

print("Visibility: {}".format(nusc.get('visibility', visibility_token)))
nusc.render_annotation(anntoken)

anntoken = '9f450bf6b7454551bbbc9a4c6e74ef2e'
visibility_token = nusc.get('sample_annotation', anntoken)['visibility_token']

print("Visibility: {}".format(nusc.get('visibility', visibility_token)))
nusc.render_annotation(anntoken)

nusc.sensor
nusc.sample_data[10]
nusc.calibrated_sensor[0]

nusc.ego_pose[0]

print("Number of `logs` in our loaded database: {}".format(len(nusc.log)))
nusc.log[0]
print("There are {} maps masks in the loaded dataset".format(len(nusc.map)))
nusc.map[0]

nusc.category[0]
cat_token = nusc.category[0]['token']
cat_token

nusc.get('category', cat_token)
nusc.sample_annotation[0]
nusc.get('visibility', nusc.sample_annotation[0]['visibility_token'])

one_instance = nusc.get('instance', nusc.sample_annotation[0]['instance_token'])
one_instance
ann_tokens = nusc.field2token('sample_annotation', 'instance_token', one_instance['token'])
ann_tokens_field2token = set(ann_tokens)

ann_tokens_field2token

ann_record = nusc.get('sample_annotation', one_instance['first_annotation_token'])
ann_record

ann_tokens_traverse = set()
ann_tokens_traverse.add(ann_record['token'])
while not ann_record['next'] == "":
    ann_record = nusc.get('sample_annotation', ann_record['next'])
    ann_tokens_traverse.add(ann_record['token'])
print(ann_tokens_traverse == ann_tokens_field2token)
nusc.list_categories()

nusc.list_attributes()
nusc.list_scenes()
nusc.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='RADAR_FRONT')
my_sample = nusc.sample[20]

# The rendering command below is commented out because it may crash in notebooks
# nusc.render_sample(my_sample['token'])
nusc.render_sample_data(my_sample['data']['CAM_FRONT'])
nusc.render_sample_data(my_sample['data']['RADAR_FRONT'], nsweeps=5, underlay_map=True)
# RadarPointCloud.disable_filters()
# nusc.render_sample_data(my_sample['data']['RADAR_FRONT'], nsweeps=5, underlay_map=True)
# RadarPointCloud.default_filters()
# nusc.render_annotation(my_sample['anns'][22])
plotter.show()
