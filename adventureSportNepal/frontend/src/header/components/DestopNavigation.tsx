import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import DropDownList from './DropDownComponent';
import { useState } from 'react';
import { AboutUs } from './MenuItems';
import { Fragment } from 'react';
import Box from '@material-ui/core/Box';
import { NavigationItemType } from '../types.d';
import { Link } from "react-router-dom";

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            width: '100%',
            display: 'flex',
            flexDirection: 'row',
            padding: 0,
        },

        listItem: {
            width: 'max-content',
        },

        hoverTransition: {
            "&:hover": {
                color: "black",
                backgroundColor: "rgba(255,255,255,0.3)"
            }
        }

    }),
);

interface CustomListItemTextProps {
    text: string;
    classes?: any;
}

const CustomListItemText = ({ text, classes }: CustomListItemTextProps) => {
    return (
        <ListItemText
            primary={text}
            className={classes.listItem}
            primaryTypographyProps={{
                variant: "h5",
            }} />
    )
}

interface IProp {
    expeditionList: undefined | NavigationItemType[]
}

export default function DesktopNavigation({ expeditionList }: IProp) {
    const classes = useStyles();
    const [isOpen, setIsOpen] = useState(false);
    const [expand, setExpand] = useState([]);

    const handleMouseEnter = (props: any) => {
        setIsOpen(true)
        setExpand(props)
    }
    const handleMouseLeave = () => {
        setIsOpen(false)
        setExpand([])
    }

    return (
        <Fragment>
            <Box onMouseLeave={() => handleMouseLeave()}>
                <List className={classes.root}>
                    <ListItem
                        button
                        component={Link}
                        to="/"
                        className={classes.hoverTransition}
                        onMouseEnter={() => handleMouseLeave()}
                    >
                        <CustomListItemText text="HOME" classes={classes} />
                    </ListItem>
                    <ListItem
                        button
                        className={classes.hoverTransition}
                        onMouseEnter={() => handleMouseEnter(expeditionList)}
                    >
                        <CustomListItemText text="EXPEDITIONS" classes={classes} />
                    </ListItem>
                    <ListItem
                        button
                        className={classes.hoverTransition}
                        onMouseEnter={() => handleMouseEnter(AboutUs)}
                    >
                        <CustomListItemText text="ABOUT US" classes={classes} />
                    </ListItem>
                    <ListItem
                        button
                        component={Link}
                        to="/faq"
                        className={classes.hoverTransition}
                        onMouseEnter={() => handleMouseLeave()}
                    >
                        <CustomListItemText text="FAQ" classes={classes} />
                    </ListItem>
                    <ListItem
                        button
                        className={classes.hoverTransition}
                        onMouseEnter={() => handleMouseLeave()}
                    >
                        <CustomListItemText text="ENQUIRE" classes={classes} />
                    </ListItem>
                </List>
                {isOpen === true && expand
                    ? (
                        <Box
                            style={{
                                minHeight: "300px",
                                position: "absolute",
                                left: "0",
                                float: "left",
                                backgroundColor: "grey",
                                width: "100vw",
                                opacity: 0.7
                            }}
                        >
                            <DropDownList dropDownItems={expand} />
                        </Box>
                    ) : null}
            </Box>
        </Fragment>
    );
}