import React, { Fragment, useEffect } from 'react';
import LandingShowCase from "../../recycle/LandingShowCase";
import FaqTabsComponent from './FaqTabsComponent';
import { useDispatch, useSelector } from "react-redux";
import { selectStatus, selectFaqPackages, getFaqPackages} from "./faqSlice";

export default function FaqComponent() {
    const dispatch = useDispatch();
    const status = useSelector(selectStatus);
    const faqPackages = useSelector(selectFaqPackages);

    useEffect(() => {
        if (status === 'idel') dispatch(getFaqPackages());
    }, [status]);

    // useEffect(() => {
    //     if (status !== 'idel') dispatch(resetStatus());
    // }, [faqPackages]);

    return (
        <Fragment>
            {faqPackages === undefined
                ? (
                    <div>Loading</div>
                ) : (
                    <Fragment>
                        <LandingShowCase />
                        <FaqTabsComponent faq_packages={faqPackages} />
                    </Fragment>
                )}
        </Fragment>
    );
}
