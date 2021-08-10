import { Box, Grid, Typography, Button }
    from '@material-ui/core';
import { useStyles } from './styles';
import SocialMedia from './components/SocialMediaComponent';
import Logo from './components/LogoComponent';
import QuickLink from './components/QuickLinkComponent';





export default function Footer() {
    const classes = useStyles();
    return (
        <Box py={8} px={5}>
            <Grid container spacing={5} alignItems={"center"}>
                <Logo />
                <QuickLink />
                <SocialMedia />
            </Grid>
        </Box>
    );
}