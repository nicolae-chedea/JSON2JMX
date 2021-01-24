from lxml import etree as ET

class JmxWriter:
    def __init__(self):
        self.root = ET.Element('jmeterTestPlan', version="1.2", properties="5.0", jmeter="5.2.1")
        self.hash1 = ET.SubElement(self.root, 'hashTree')

    def add_test_plan(self, test_plan_name="Test Plan", test_plan_comment=""):
        test_plan = ET.SubElement(self.hash1, 'TestPlan', guiclass="TestPlanGui", testclass="TestPlan", testname=test_plan_name, enabled="true")
        test_plan_comments = ET.SubElement(test_plan, 'stringProp', name="TestPlan.comments")
        test_plan_comments.text = test_plan_comment
        test_plan_functional = ET.SubElement(test_plan, 'boolProp', name="TestPlan.functional_mode")
        test_plan_functional.text = "false"
        tearDown_on_shutdown = ET.SubElement(test_plan, 'boolProp', name="TestPlan.tearDown_on_shutdown")
        tearDown_on_shutdown.text = "true"
        serialize_threadgroups = ET.SubElement(test_plan, 'boolProp', name="TestPlan.serialize_threadgroups")
        serialize_threadgroups.text = "false"
        user_defined_variables = ET.SubElement(test_plan, 'elementProp', name="TestPlan.user_defined_variables", elementType="Arguments", guiclass="ArgumentsPanel", testclass="Arguments", testname="User Defined Variables", enabled="true")
        arguments = ET.SubElement(user_defined_variables, 'collectionProp', name="Arguments.arguments")
        user_define_classpath = ET.SubElement(test_plan, 'stringProp', name="TestPlan.user_define_classpath")

    def add_threadgroup(self, threadgroup_name="Thread Group"):
        hash = ET.SubElement(self.hash1, 'hashTree')
        threadgroup = ET.SubElement(hash, 'ThreadGroup', guiclass="ThreadGroupGui", testclass="ThreadGroup", testname=threadgroup_name, enabled="true")
        main_controller = ET.SubElement(threadgroup, 'elementProp', name="ThreadGroup.main_controller", elementType="LoopController", guiclass="LoopControlPanel", testclass="LoopController", enabled="true")
        continue_forever = ET.SubElement(main_controller, 'boolProp', name="LoopController.continue_forever")
        continue_forever.text = "false"
        loops = ET.SubElement(main_controller, 'intProp', name="LoopController.loops")
        loops.text = "1"
        num_threads = ET.SubElement(threadgroup, 'intProp', name="ThreadGroup.num_threads")
        num_threads.text = "1"
        ramp_time = ET.SubElement(threadgroup, 'intProp', name="ThreadGroup.ramp_time")
        ramp_time.text = "1"
        scheduler = ET.SubElement(threadgroup, 'boolProp', name="ThreadGroup.scheduler")
        scheduler.text = "false"
        duration = ET.SubElement(threadgroup, 'longProp', name="ThreadGroup.duration")
        duration.text = ""
        delay = ET.SubElement(threadgroup, 'longProp', name="ThreadGroup.delay")
        delay.text = ""
        same_user_on_next_iteration = ET.SubElement(threadgroup, 'boolProp', name="ThreadGroup.same_user_on_next_iteration")
        same_user_on_next_iteration.text = "true"

    def write_xml(self, file_name):
        tree = ET.ElementTree(self.root)
        with open(file_name, 'wb') as f:
            tree.write(f, encoding="UTF-8", xml_declaration=True, pretty_print=True)

if __name__ == '__main__':
    jmx = JmxWriter()
    jmx.add_test_plan('Auth')
    jmx.add_threadgroup()
    # jmx.add_http_sampler()
    jmx.write_xml('output14.jmx')
