import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import { useStyles } from '../style';
import DrawerData from './DrawerDataComponent';
import { useState } from 'react';


interface Props {
    isDrawerOpen: boolean;
    handleDrawerToggle: any;
    drawerTransitionMiliSecond: number;
    expeditionList: any
}

class Stack {
    items: any;

    constructor() {
        this.items = [];
    }

    push(element: any): void {
        // push element into the items
        this.items.push(element);
    }
    pop() {
        if (this.items.length == 0) {
            console.log("underflow");
            return
        }
        return this.items.pop();
    }
    peek() {
        return this.items[this.items.length - 1];
    }
    tos() {
        return this.items.length;
    }
    isEmpty() {
        return this.items.length == 0;
    }

}

interface InitialStackInterface {
    [index: number]: {
        name: string
        items: any
    }
}

const InitialStack: InitialStackInterface = [
    {
        name: "HOME",
        items: []
    },
    {
        name: "EXPEDITION",
        items: []
    },
    {
        name: "ABOUT US",
        items: []
    },
    {
        name: "FAQ",
        items: []
    },
    {
        name: "ENQUIRY",
        items: []
    }
]


export default function NavigationDrawer(props: Props) {
    const {
        isDrawerOpen,
        handleDrawerToggle,
        drawerTransitionMiliSecond, expeditionList } = props;
    const classes = useStyles();
    const stack = new Stack();
    stack.push(InitialStack);
    const [state, setState] = useState(new Array(InitialStack));
    const handleOnClose = () => {
        setState(new Array(InitialStack));
        handleDrawerToggle();
    }
    return (
        <div className={classes.root}>
            <CssBaseline />
            <nav className={classes.drawer} aria-label="mailbox folders">
                <Drawer
                    variant="temporary"
                    anchor={"left"}
                    open={isDrawerOpen}
                    onClose={handleOnClose}
                    classes={{
                        paper: classes.drawerPaper,
                    }}
                    ModalProps={{
                        keepMounted: true,
                    }}
                    transitionDuration={drawerTransitionMiliSecond}
                >
                    <DrawerData
                        classes={classes}
                        handleDrawerToggle={handleOnClose}
                        state={state}
                        setState={setState}
                        expeditionList={expeditionList}
                    />
                </Drawer>
            </nav>

        </div>
    );
}
