import nuke
print "importing Nuke ..."


def set_context():
    parent = nuke.thisNode()
    return parent


def create_frame_hold_nodes(start,end,input):
    for i in range(start,end):
        fh = nuke.createNode("FrameHold", inpanel=False)
        fh['first_frame'].setValue(i)
        fh.setInput(0, input)
    print str(len(range(start,end))) + " " "FrameHold nodes created"
    return


def select_frame_hold_nodes():
    nodes = [i for i in nuke.allNodes() if i.Class() == "FrameHold"]
    return nodes


def collect_frame_hold_selection_names(sl):
    name = ""
    ls = []

    for i in sl:
        name = i.name()
        ls.append(name)
    ls.reverse()
    return ls


def set_merge_operation_over():
    for i in nuke.allNodes():
        if i.Class() == "Merge2":
            i['operation'].setValue("over")
    bg = nuke.toNode('C')
    print bg
    bg['color'].setValue(0)


def set_merge_operation_max():
    for i in nuke.allNodes():
        if i.Class() == "Merge2":
            i['operation'].setValue("max")
    bg = nuke.toNode('C')
    print bg
    bg['color'].setValue(0)

def set_merge_operation_minus():
    for i in nuke.allNodes():
        if i.Class() == "Merge2":
            i['operation'].setValue("minus")
    bg = nuke.toNode('C')
    print bg
    bg['color'].setValue(0)


def set_merge_operation_average():
    for i in nuke.allNodes():
        if i.Class() == "Merge2":
            i['operation'].setValue("average")
    bg = nuke.toNode('C')
    print bg
    bg['color'].setValue(1)


def set_merge_operation_min():
    for i in nuke.allNodes():
        if i.Class() == "Merge2":
            i['operation'].setValue("min")
    bg = nuke.toNode('C')
    print bg
    bg['color'].setValue(1)

def create_merge_nodes(ls1,ls2):
    parent = set_context()
    mode_1 = parent['mode_1'].value()
    #retract = parent['retract'].value()
    for i in range(len(ls1)):
        d = nuke.nodes.Merge2(name=str(i + 1))
        d.setInput(1, nuke.toNode(ls2[i]))
        if d.name() == "1":
            pass
        else:
            #d.setInput(2, nuke.toNode(str(i)))
            pass
        d['operation'].setValue(str(mode_1))
        d['disable'].setExpression("[python {nuke.toNode('Control')['retract'].value()}] >  [python {nuke.thisNode().name()}] ? 1 : 0")
    print str(len(ls1)) + " " + "Merge nodes created"
    return


def select_merge_nodes():
    nodes = [i for i in nuke.allNodes() if i.Class() == "Merge2"]
    return nodes


def connect_merge_nodes_to_each_other(ls):
    for i in ls:
        n = i.name()
        c = nuke.toNode(n)
        d = nuke.toNode(str(int(n) - 1))
        i.setInput(0, d)
    return


def connect_switch_node(ls,sn):
    for i in range(len(ls)):
        m = ls[i]
        sn.setInput(i, m)
    return


def create_multiply_nodes(sl):
    parent = set_context()

    for i in range(len(sl)):
        mul = nuke.createNode("Multiply", inpanel=False)
        mul.setInput(0,nuke.toNode(sl[i]))
        mul['mix'].setExpression('parent.smooth')

    values = create_value_list(sl)
    return values


def create_value_list(ls):
    values = []
    temp = 0
    for i in range(len(ls)+1):
        if i == 0:
            temp = 0
            values.append(temp)
        else:
            temp = round(i / (float(len(ls)+1)), 4)
            values.append(temp)
    return values


def square_values(ls):
    squared_values = []
    temp = 0
    for i in ls:
        temp = i * i
        squared_values.append(temp)
    return squared_values


def double_square_values(ls):
    squared_values = []
    temp = 0
    for i in ls:
        temp = i * i * i * i
        squared_values.append(temp)
    return squared_values


def apply_multiply_lin_value():
    try:
        multiply_nodes = select_multiply_nodes()
        name_list = collect_multiply_selection_names(multiply_nodes)
        values = create_value_list(name_list)
        for i in range(len(name_list)):
            nuke.toNode(name_list[i])['value'].setValue(values[i])
        return
    except:
        raise ValueError('run the tool first, dude')
        return

def apply_reversed_multiply_lin_value():
    try:
        multiply_nodes = select_multiply_nodes()
        name_list = collect_multiply_selection_names_invert(multiply_nodes)
        values = create_value_list(name_list)
        for i in range(len(name_list)):
            nuke.toNode(name_list[i])['value'].setValue(values[i])
        return
    except:
        raise ValueError('run the tool first, dude')
        return


def apply_multiply_sq_value():
    try:
        multiply_nodes = select_multiply_nodes()
        name_list = collect_multiply_selection_names(multiply_nodes)
        values = create_value_list(name_list)
        sq_values = square_values(values)
        for i in range(len(name_list)):
            nuke.toNode(name_list[i])['value'].setValue(sq_values[i])
        return
    except:
        raise ValueError('run the tool first, dude')
        return

def apply_reversed_multiply_sq_value():
    try:
        multiply_nodes = select_multiply_nodes()
        name_list = collect_multiply_selection_names_invert(multiply_nodes)
        values = create_value_list(name_list)
        sq_values = square_values(values)
        for i in range(len(name_list)):
            nuke.toNode(name_list[i])['value'].setValue(sq_values[i])
        return
    except:
        raise ValueError('run the tool first, dude')
        return


def apply_multiply_double_sq_value():
    try:
        multiply_nodes = select_multiply_nodes()
        name_list = collect_multiply_selection_names(multiply_nodes)
        values = create_value_list(name_list)
        double_sq_values = double_square_values(values)
        for i in range(len(name_list)):
            nuke.toNode(name_list[i])['value'].setValue(double_sq_values[i])
        return
    except:
        raise ValueError('run the tool first, dude')
        return

def apply_inverted_multiply_double_sq_value():
    try:
        multiply_nodes = select_multiply_nodes()
        name_list = collect_multiply_selection_names_invert(multiply_nodes)
        values = create_value_list(name_list)
        double_sq_values = double_square_values(values)
        for i in range(len(name_list)):
            nuke.toNode(name_list[i])['value'].setValue(double_sq_values[i])
        return
    except:
        raise ValueError('run the tool first, dude')


def apply_multiply_value(multnodes,valuelist):
    for i in range(len(multnodes)):
        nuke.toNode(multnodes[i])['value'].setValue(valuelist[i])
    return


def select_multiply_nodes():
    nodes = [i for i in nuke.allNodes() if i.Class() == "Multiply"]
    return nodes


def collect_multiply_selection_names(sl):
    name = ""
    ls = []

    for i in sl:
        name = i.name()
        ls.append(name)

    return ls

def collect_multiply_selection_names_invert(sl):
    name = ""
    ls = []

    for i in sl:
        name = i.name()
        ls.append(name)
    ls.reverse()

    return ls



def reduce_density_1():

    node_name_list = collect_multiply_selection_names(select_merge_nodes())
    factor = 0

    for i in node_name_list:
        nuke.toNode(i)['mix'].setValue(1)
        nuke.toNode(i)['tile_color'].setValue(0)

    for i in node_name_list:
        if int(i) % factor == 0:
            nuke.toNode(i)['mix'].setValue(0)
            nuke.toNode(i)['tile_color'].setValue(3238002943)

    return


def reduce_density_2():

    node_name_list = collect_multiply_selection_names(select_merge_nodes())
    factor = 2

    for i in node_name_list:
        nuke.toNode(i)['mix'].setValue(1)
        nuke.toNode(i)['tile_color'].setValue(0)

    for i in node_name_list:
        if int(i) % factor == 0:
            nuke.toNode(i)['mix'].setValue(0)
            nuke.toNode(i)['tile_color'].setValue(3238002943)

    return


def reduce_density_3():

    node_name_list = collect_multiply_selection_names(select_merge_nodes())
    factor = 3

    for i in node_name_list:
        nuke.toNode(i)['mix'].setValue(1)
        nuke.toNode(i)['tile_color'].setValue(0)

    for i in node_name_list:
        if int(i) % factor == 0:
            nuke.toNode(i)['mix'].setValue(0)
            nuke.toNode(i)['tile_color'].setValue(3238002943)

    return


def reduce_density_4():

    node_name_list = collect_multiply_selection_names(select_merge_nodes())
    factor = 4

    for i in node_name_list:
        nuke.toNode(i)['mix'].setValue(1)
        nuke.toNode(i)['tile_color'].setValue(0)

    for i in node_name_list:
        if int(i) % factor == 0:
            nuke.toNode(i)['mix'].setValue(0)
            nuke.toNode(i)['tile_color'].setValue(3238002943)

    return


def run():
    # CLEAN UP GIZMO
    reset()
    #GET GROUP AS CONTEXT
    parent = set_context()

    #GET GROUP'S KNOBS VALUES
    i = int(parent['from'].value())
    o = int(parent['to'].value())
    invert_ramp = parent['invert_ramp'].value()


    #GET GROUP'S PREEXISTING NODES AS VARIABLES FOR LATER USE
    img = nuke.toNode('R')
    sw = nuke.toNode('SW')

    #CREATE FRAMEHOLD NODES AND COLLECT THEIR NAMES FOR LATER USE
    create_frame_hold_nodes(i,o,img)
    sel = select_frame_hold_nodes()
    sel1 = collect_frame_hold_selection_names(sel)

    # CREATE MULTIPLY NODES
    multiply_nodes = create_multiply_nodes(sel1)
    sqrt_values = square_values(multiply_nodes)
    sel = select_multiply_nodes()
    sel1 = []
    if invert_ramp == False:
        sel1 = collect_multiply_selection_names(sel)
    elif invert_ramp == True:
        sel1 = collect_multiply_selection_names_invert(sel)
    else:
        pass

    #CREATE MERGE NODES AND CONNECT THEM TO THE FRAMEHOLD NODES AND TO EACH OTHER.
    create_merge_nodes(sel,sel1)
    msel = select_merge_nodes()
    first_merge = msel[-1]
    connect_merge_nodes_to_each_other(msel)

    #CONNECT SWITCH NODE INPUTS
    connect_switch_node(msel,sw)

    #FINALIZE GROUP'S SET UP
    C = nuke.toNode('C')
    C['format'].setExpression('R.format')
    mask_input =  nuke.toNode('mask_input')
    bo = nuke.toNode('bo')
    output = nuke.toNode('Output1')
    output.setInput(0, bo)
    first_merge.setInput(0, C)

    #ORGANIZE NODES A LITTLE
    auto_place()

    print "Written by Boris Martinez in 2018"

    return

def reset():
    for i in nuke.allNodes():
        if i.Class() == 'Constant' or i.Class() == 'Input' or i.Class() == 'Output' or i.Class() \
                == 'Viewer' or i.Class() == 'Reformat' or i.Class() == 'Switch' or  i.Class() == 'Grade'\
                or i.Class() == 'NoOp' or i.Class() == 'Keymix' or  i.Class() == 'BlackOutside'  \
                or  i.Class() == 'CopyBBox':
            pass
        else:
            nuke.delete(i)

def auto_place():
    all = nuke.allNodes()
    for i in all:
        i.autoplace()

    yield all
