import React from 'react';
import {shallow} from 'enzyme';
import Exercise1 from '../Exercise1';

describe('Exercise1', () => {
  describe('Exercise1', () => {
    it('should print 26 li', () => {
      const wrapper = shallow(
        <Exercise1 />,
      );
      const li = wrapper.find('li');
      expect(li).toHaveLength(26);
    });
    it('should print 26 letters for line', () => {
      const wrapper = shallow(
        <Exercise1 />,
      );
      const li = wrapper.find('li');
      expect(li.length).toEqual(26);
    });
  });
});
