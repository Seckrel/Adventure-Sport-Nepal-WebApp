import {
    Box,
    IconButton,
    Divider,
    List,
    ListItem,
    ListItemText,
    Typography,
    Grid,
    Button
} from '@material-ui/core';
import { Fragment } from 'react';
import { Link, useHistory } from 'react-router-dom';
import CloseIcon from '@material-ui/icons/Close';
import ArrowForwardIosIcon from '@material-ui/icons/ArrowForwardIos';

const ABOUTUS = [
    { name: "Our Team", href: "/ourteam" },
    { name: "Safety", href: "/saftey" }
]

const InitMenu = ({ state, expeditionList, setState, closeDrawer }: any) => {
    const history = useHistory();
    const handleClick = (name: string) => {
        switch (name) {
            case "EXPEDITION":
                setState((old: any) => [...old, expeditionList]);
                break;
            case "ABOUT US":
                setState((old: any) => [...old, ABOUTUS]);
                break;
            case "treking":
                setState((old: any) => [...old, expeditionList.find((obj: any) => obj.name == "treking").items]);
                break;
            case "sking":
                setState((old: any) => [...old, expeditionList.find((obj: any) => obj.name == "sking").items]);
                break;
            case "FAQ":
                history.push('/faq');
                closeDrawer();
                break;
            default:
                history.push('/');
                closeDrawer();
            // Add more case for enquiry
        }
    }
    
    return (
        <List>
            {state.at(-1).map((obj: any) =>
                obj.hasOwnProperty('items')
                    ? (
                        <ListItem
                            button
                            onClick={() => handleClick(obj.name)}
                        >
                            <ListItemText primary={(obj.name).toUpperCase()} />
                        </ListItem>
                    ) : (
                        <ListItem
                            button
                            component={Link}
                            to={obj.href}
                            onClick={closeDrawer}
                        >
                            <ListItemText primary={(obj.name).toUpperCase()} />
                        </ListItem>
                    )
            )}
        </List>
    );
}


export default function DrawerData(props: any) {
    const { classes,
        handleDrawerToggle,
        state,
        setState,
        expeditionList } = props;

    const goBack = () => {
        state.splice(-1, 1);
        console.log("eunning", state);
        setState([...state]);
    }

    return (
        <Fragment>
            {console.log(state)}
            <Grid container>
                <Grid item xs={12}>
                    {state.length > 1 &&
                        (<Button
                            onClick={goBack}
                        >
                            back </Button>)
                    }
                    <Button onClick={handleDrawerToggle}> X </Button>
                </Grid>
                <Grid item xs={12}>
                    <InitMenu
                        state={state}
                        setState={setState}
                        expeditionList={expeditionList}
                        closeDrawer={handleDrawerToggle}
                    />
                </Grid>
            </Grid>
        </Fragment>
    );

};